#!/usr/bin/env python3
"""
通用 Skill 包装器 - 跨平台抽象层

使用示例:
    from skill_wrapper import SkillRunner
    
    runner = SkillRunner(
        skill_name='format-python',
        tool_command=['black', '{path}'],
        check_command=['black', '--version']
    )
    
    result = runner.run(
        path='.',
        check_mode=False,
        verbose=False
    )
"""

import subprocess
import sys
import shutil
from pathlib import Path
from typing import List, Optional, Dict


class SkillRunner:
    """统一的跨平台 Skill 执行器"""
    
    # ANSI 颜色代码
    COLORS = {
        'RED': '\033[0;31m',
        'GREEN': '\033[0;32m',
        'YELLOW': '\033[1;33m',
        'CYAN': '\033[0;36m',
        'GRAY': '\033[0;90m',
        'RESET': '\033[0m'
    }
    
    def __init__(self, skill_name: str, tool_command: List[str], 
                 check_command: Optional[List[str]] = None):
        """
        初始化 Skill 执行器
        
        Args:
            skill_name: Skill 名称（如 'format-python'）
            tool_command: 工具命令模板（如 ['black', '{path}']）
            check_command: 检测工具是否安装的命令（如 ['black', '--version']）
        """
        self.skill_name = skill_name
        self.tool_command = tool_command
        self.check_command = check_command or [tool_command[0], '--version']
        self.tool_name = tool_command[0]
    
    def _print(self, message: str, color: str = 'RESET'):
        """带颜色的打印（跨平台）"""
        # Windows 10+ 支持 ANSI，但为了兼容性检查
        if sys.platform == 'win32':
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except Exception:
                # 如果启用 ANSI 失败，禁用颜色
                print(message)
                return
        
        print(f"{self.COLORS.get(color, '')}{message}{self.COLORS['RESET']}")
    
    def check_tool(self) -> bool:
        """检测工具是否已安装"""
        # 方法 1: 使用 shutil.which
        if shutil.which(self.tool_name):
            return True
        
        # 方法 2: 尝试运行检测命令
        try:
            result = subprocess.run(
                self.check_command,
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False
    
    def install_tool(self, package_name: Optional[str] = None) -> bool:
        """尝试自动安装工具（Python 包）"""
        pkg = package_name or self.tool_name
        
        self._print(f"⚠️  警告: 未检测到 {self.tool_name}", 'YELLOW')
        self._print("")
        self._print(f"📥 正在尝试安装 {pkg}...", 'CYAN')
        
        try:
            # 优先使用 pip3（如果存在）
            pip_cmd = 'pip3' if shutil.which('pip3') else 'pip'
            
            result = subprocess.run(
                [pip_cmd, 'install', pkg, '--quiet'],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                self._print(f"✅ {pkg} 安装成功!", 'GREEN')
                # 验证安装
                version = subprocess.run(
                    self.check_command,
                    capture_output=True,
                    text=True
                ).stdout.strip()
                self._print(f"   版本: {version}", 'GREEN')
                return True
            else:
                raise Exception(result.stderr)
        
        except Exception as e:
            self._print(f"❌ 自动安装失败: {e}", 'RED')
            self._print("")
            self._print(f"💡 请手动安装:", 'CYAN')
            self._print(f"   pip install {pkg}", 'YELLOW')
            self._print("")
            self._print(f"   或使用 pipx（推荐）:", 'CYAN')
            self._print(f"   pipx install {pkg}", 'CYAN')
            return False
    
    def run(self, path: str = '.', check_mode: bool = False, 
            verbose: bool = False, **kwargs) -> int:
        """
        执行 Skill 任务
        
        Args:
            path: 目标路径
            check_mode: 仅检查不修改
            verbose: 详细输出
            **kwargs: 其他工具特定参数
        
        Returns:
            退出代码（0 = 成功）
        """
        self._print(f"🎨 {self.skill_name} - 正在处理...", 'CYAN')
        self._print("")
        
        # 1. 检测工具
        if not self.check_tool():
            if not self.install_tool():
                return 1
        else:
            # 显示工具版本
            version = subprocess.run(
                self.check_command,
                capture_output=True,
                text=True
            ).stdout.strip()
            self._print(f"✅ {self.tool_name}: {version}", 'GREEN')
        
        self._print("")
        self._print("━" * 50, 'GRAY')
        
        # 2. 构建命令
        cmd = []
        for part in self.tool_command:
            if '{path}' in part:
                cmd.append(part.replace('{path}', path))
            else:
                cmd.append(part)
        
        if check_mode:
            cmd.append('--check')
            self._print("🔍 检查模式: 仅检查不修改", 'YELLOW')
            self._print("")
        
        if verbose:
            cmd.append('--verbose')
        
        # 添加其他参数
        for key, value in kwargs.items():
            if isinstance(value, bool) and value:
                cmd.append(f'--{key.replace("_", "-")}')
            elif not isinstance(value, bool):
                cmd.append(f'--{key.replace("_", "-")}')
                cmd.append(str(value))
        
        # 3. 执行命令
        self._print("🚀 开始执行...", 'GREEN')
        self._print("")
        
        try:
            result = subprocess.run(cmd, check=False)
            exit_code = result.returncode
        except KeyboardInterrupt:
            self._print("\n⚠️ 用户中断", 'YELLOW')
            return 130
        except Exception as e:
            self._print(f"❌ 执行错误: {e}", 'RED')
            return 1
        
        # 4. 输出结果
        self._print("")
        self._print("━" * 50, 'GRAY')
        
        if exit_code == 0:
            if check_mode:
                self._print("✅ 检查通过: 未发现问题!", 'GREEN')
            else:
                self._print("✅ 任务完成!", 'GREEN')
        else:
            if check_mode:
                self._print("⚠️  检查失败: 发现问题", 'YELLOW')
                self._print("   请运行不带 --check 参数的命令以自动修复", 'GRAY')
            else:
                self._print("❌ 任务失败", 'RED')
        
        self._print("")
        return exit_code


# 快捷函数
def format_python(path: str = '.', check: bool = False, verbose: bool = False) -> int:
    """Python 代码格式化快捷函数"""
    runner = SkillRunner('format-python', ['black', '{path}'])
    return runner.run(path, check_mode=check, verbose=verbose)


def lint_python(path: str = '.', fix: bool = False, verbose: bool = False) -> int:
    """Python 代码检查快捷函数"""
    cmd = ['ruff', 'check', '{path}']
    if fix:
        cmd.append('--fix')
    
    runner = SkillRunner('lint-python', cmd, ['ruff', '--version'])
    return runner.run(path, check_mode=not fix, verbose=verbose)


if __name__ == '__main__':
    # 简单的 CLI 测试
    import argparse
    
    parser = argparse.ArgumentParser(description='Skill 包装器测试')
    parser.add_argument('path', nargs='?', default='.', help='目标路径')
    parser.add_argument('--check', action='store_true', help='检查模式')
    parser.add_argument('--verbose', action='store_true', help='详细输出')
    
    args = parser.parse_args()
    
    # 测试 black
    exit_code = format_python(args.path, args.check, args.verbose)
    sys.exit(exit_code)
