#!/usr/bin/env python3
"""
自动状态生成器 - 监控项目变化并更新 status.md

功能：
1. 自动检测技术栈（从 package.json, requirements.txt 等）
2. 统计项目规模（文件数、代码行数）
3. 分析目录结构
4. 保留用户手动编辑的内容
"""

import os
import json
import datetime
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# --- 引入共享配置 ---
# auto_status.py 通常在 context/ 目录下，需要向上一级导入
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

try:
    from scripts.config import IGNORE_DIRS, EXTENSIONS, PROJECT_ROOT
except ImportError:
    # Fallback
    IGNORE_DIRS = {'.git', '__pycache__', 'node_modules', 'context', '.gemini', '.history'}
    EXTENSIONS = {'.py', '.md', '.json', '.js', '.vue', '.ps1', '.sh', '.txt'}
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    print("⚠️  Warning: Could not import scripts.config, using fallback defaults.")

# 统计信息
WARNINGS = []


def add_warning(msg: str):
    """记录运行中的警告"""
    WARNINGS.append(msg)
    print(f"  ⚠️  {msg}")

# 依赖文件映射
DEPENDENCY_FILES = {
    'requirements.txt': 'Python',
    'Pipfile': 'Python (Pipenv)',
    'pyproject.toml': 'Python (Poetry)',
    'package.json': 'Node.js',
    'pom.xml': 'Java (Maven)',
    'build.gradle': 'Java (Gradle)',
    'Cargo.toml': 'Rust',
    'go.mod': 'Go',
    'Gemfile': 'Ruby',
    'composer.json': 'PHP',
    '*.csproj': 'C# (.NET)',
}


def detect_tech_stack(root_path: str = '.') -> Dict[str, List[str]]:
    """检测项目技术栈"""
    detected = {}
    
    for dep_file, tech_name in DEPENDENCY_FILES.items():
        if '*' in dep_file:
            # 处理通配符（如 *.csproj）
            pattern = dep_file.replace('*', '')
            for file in Path(root_path).rglob(f'*{pattern}'):
                if file.is_file():
                    detected[tech_name] = detected.get(tech_name, []) + [str(file)]
        else:
            file_path = Path(root_path) / dep_file
            if file_path.exists():
                detected[tech_name] = [str(file_path)]
    
    return detected


def extract_dependencies(tech_stack: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """从依赖文件中提取主要依赖"""
    dependencies = {}
    
    for tech, files in tech_stack.items():
        deps = []
        for file_path in files:
            if 'package.json' in file_path:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        all_deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
                        deps = list(all_deps.keys())[:5]
                except (json.JSONDecodeError, PermissionError) as e:
                    add_warning(f"无法读取 package.json ({file_path}): {e}")
                except Exception as e:
                    add_warning(f"解析 package.json 时出错: {e}")
            elif 'requirements.txt' in file_path:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = [line.split('==')[0].split('>=')[0].strip() 
                                for line in f if line.strip() and not line.startswith('#')]
                        deps = lines[:5]
                except Exception as e:
                    add_warning(f"读取 requirements.txt ({file_path}) 时出错: {e}")
        
        if deps:
            dependencies[tech] = deps
    
    return dependencies


def get_project_analysis(root_path: str = '.', max_depth: int = 2) -> Tuple[int, int, str]:
    """单次遍历项目，获取文件数、行数和目录结构"""
    file_count = 0
    line_count = 0
    structure = []
    
    for root, dirs, files in os.walk(root_path):
        # 计算当前深度
        rel_root = os.path.relpath(root, root_path)
        level = 0 if rel_root == '.' else rel_root.count(os.sep) + 1
        
        # 过滤忽略目录
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        # 1. 统计文件和行数
        matched_files = [f for f in files if any(f.endswith(ext) for ext in EXTENSIONS)]
        for file in matched_files:
            file_count += 1
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    line_count += sum(1 for line in f if line.strip())
            except (PermissionError, OSError) as e:
                add_warning(f"无法读取文件 {file_path}: {e}")
            except Exception as e:
                add_warning(f"统计文件 {file_path} 行数时出错: {e}")

        # 2. 生成目录结构（限制深度）
        if level < max_depth:
            indent = '  ' * level
            structure.append(f"{indent}- {os.path.basename(root) if rel_root != '.' else 'ROOT'}/")
            for file in matched_files[:5]:
                structure.append(f"{indent}  - {file}")
            if len(matched_files) > 5:
                structure.append(f"{indent}  - ... ({len(matched_files)-5} more files)")
    
    return file_count, line_count, '\n'.join(structure)


def read_manual_section(status_file: str) -> str:
    """读取 status.md 中用户手动维护的部分（使用正则匹配）"""
    default_manual = """### 当前开发焦点
_请在此处记录当前正在进行的工作_

### 已知问题
_可选：记录当前已知但未修复的问题_

### 下一步计划
_可选：记录即将进行的开发任务_"""

    if not os.path.exists(status_file):
        return default_manual
    
    try:
        with open(status_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # 使用正则匹配 ## ✍️ 手动维护区域 到 下一个 --- 之间的内容
            pattern = r'## ✍️ 手动维护区域\s*(.*?)\s*(?=\n---|$)'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                manual_content = match.group(1).strip()
                # 额外保护：如果匹配到了自动更新提示，则截断
                if '## 🔄 更新此文件' in manual_content:
                    manual_content = manual_content.split('## 🔄 更新此文件')[0].strip()
                return manual_content if manual_content else default_manual
    except Exception as e:
        add_warning(f"读取手动区域时出错: {e}")
    
    return default_manual


def generate_status_md(root_path: str, file_count: int, line_count: int, dir_structure: str) -> str:
    """Generate status.md content (AI-friendly English format)"""
    # 1. Detect tech stack
    tech_stack = detect_tech_stack(root_path)
    dependencies = extract_dependencies(tech_stack)
    
    # 2. Read manual section
    manual_section = read_manual_section(os.path.join(root_path, 'context', 'status.md'))
    
    # 3. Current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 4. Build Markdown
    tech_stack_md = ""
    if tech_stack:
        for tech, files in tech_stack.items():
            tech_stack_md += f"- **{tech}**"
            if tech in dependencies and dependencies[tech]:
                deps_str = ', '.join(dependencies[tech])
                tech_stack_md += f" (Main Deps: {deps_str})"
            tech_stack_md += f"\n  - Detected from: `{os.path.basename(files[0])}`\n"
    else:
        tech_stack_md = "_No standard dependency files detected_"
    
    content = f"""# Project Status Snapshot (AI-Centric)

> **NOTE**: This file is automatically maintained by `context/auto_status.py`.
> DO NOT manually edit the "Auto-Generated" section.

---

## 📊 Auto-Generated Section

**Last Updated**: {current_time}  
**Project Scale**: {file_count} files, {line_count:,} lines of code

### Technology Stack
{tech_stack_md}

### Project Structure (Max Depth: 2)
```
{dir_structure}
```

---

## ✍️ Manual Maintenance Section

{manual_section}

---

## 🔄 Refresh Status

Run the following command to refresh this file:

```bash
python context/auto_status.py
```
"""
    return content


def main():
    """主函数"""
    print("🔄 正在分析项目状态...")
    
    # 切换到项目根目录 (统一使用 PROJECT_ROOT)
    os.chdir(PROJECT_ROOT)
    
    # 单次遍历完成所有统计
    file_count, line_count, dir_structure = get_project_analysis('.')
    
    # 生成内容
    content = generate_status_md('.', file_count, line_count, dir_structure)
    
    # 写入文件
    output_file = 'context/status.md'
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 状态文件已更新: {output_file}")
    except Exception as e:
        print(f"❌ 写入状态文件失败: {e}")
        return

    # 输出运行报告
    print("\n📋 运行报告:")
    print(f"  - 文件数: {file_count}")
    print(f"  - 代码行数: {line_count:,}")
    
    if WARNINGS:
        print(f"\n⚠️  发现 {len(WARNINGS)} 个警告:")
        for warn in WARNINGS[:5]:
            print(f"  - {warn}")
        if len(WARNINGS) > 5:
            print(f"  - ... 及其他 {len(WARNINGS)-5} 个警告")
    else:
        print("\n✨ 运行成功，未发现逻辑警告。")


if __name__ == '__main__':
    main()
