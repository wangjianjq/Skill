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
from pathlib import Path
from typing import Dict, List, Tuple

# 复用 make_prompt.py 的配置
IGNORE_DIRS = {'.git', '__pycache__', 'node_modules', 'context', '.gemini', '.history'}
EXTENSIONS = {'.py', '.md', '.json', '.js', '.vue', '.ps1', '.sh', '.txt', '.ts', '.tsx', '.jsx'}

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
                        # 提取主要依赖（前5个）
                        all_deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
                        deps = list(all_deps.keys())[:5]
                except Exception:
                    pass
            elif 'requirements.txt' in file_path:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = [line.split('==')[0].split('>=')[0].strip() 
                                for line in f if line.strip() and not line.startswith('#')]
                        deps = lines[:5]
                except Exception:
                    pass
        
        if deps:
            dependencies[tech] = deps
    
    return dependencies


def count_project_stats(root_path: str = '.') -> Tuple[int, int]:
    """统计项目文件数和代码行数"""
    file_count = 0
    line_count = 0
    
    for root, dirs, files in os.walk(root_path):
        # 过滤忽略目录
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            if any(file.endswith(ext) for ext in EXTENSIONS):
                file_count += 1
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                        line_count += sum(1 for line in f if line.strip())
                except Exception:
                    pass
    
    return file_count, line_count


def get_directory_structure(root_path: str = '.', max_depth: int = 2) -> str:
    """获取项目目录结构（限制深度）"""
    structure = []
    
    for root, dirs, files in os.walk(root_path):
        # 计算当前深度
        level = root.replace(root_path, '').count(os.sep)
        if level >= max_depth:
            dirs[:] = []  # 不再深入子目录
            continue
        
        # 过滤忽略目录
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        indent = '  ' * level
        structure.append(f"{indent}- {os.path.basename(root)}/")
        
        # 只列出关键文件（不超过5个）
        key_files = [f for f in files if any(f.endswith(ext) for ext in EXTENSIONS)][:5]
        for file in key_files:
            structure.append(f"{indent}  - {file}")
    
    return '\n'.join(structure)


def read_manual_section(status_file: str) -> str:
    """读取 status.md 中用户手动维护的部分"""
    if not os.path.exists(status_file):
        return """### 当前开发焦点
_请在此处记录当前正在进行的工作_

### 已知问题
_可选：记录当前已知但未修复的问题_

### 下一步计划
_可选：记录即将进行的开发任务_"""
    
    try:
        with open(status_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # 提取 "手动维护区域" 部分
            marker = '## ✍️ 手动维护区域'
            if marker in content:
                start = content.index(marker)
                # 跳过标题行本身，从下一行开始搜索分隔符
                after_marker = start + len(marker)
                # 查找下一个 '---' 分隔符（独占一行）
                remaining = content[after_marker:]
                end_offset = None
                for line_start in range(len(remaining)):
                    if remaining[line_start:].startswith('---'):
                        # 确保 '---' 在行首（前一个字符是换行或在开头）
                        if line_start == 0 or remaining[line_start - 1] == '\n':
                            end_offset = line_start
                            break
                if end_offset is not None:
                    manual_section = remaining[:end_offset].strip()
                else:
                    manual_section = remaining.strip()
                # 去掉最后的分隔符前的内容
                if '## 🔄 更新此文件' in manual_section:
                    manual_section = manual_section.split('## 🔄 更新此文件')[0].strip()
                return manual_section if manual_section else "### 当前开发焦点\n_请在此处记录_"
    except Exception:
        pass
    
    return "### 当前开发焦点\n_请在此处记录_"


def generate_status_md(root_path: str = '.') -> str:
    """生成完整的 status.md 内容"""
    # 1. 检测技术栈
    tech_stack = detect_tech_stack(root_path)
    dependencies = extract_dependencies(tech_stack)
    
    # 2. 统计项目规模
    file_count, line_count = count_project_stats(root_path)
    
    # 3. 获取目录结构
    dir_structure = get_directory_structure(root_path)
    
    # 4. 读取手动维护的部分
    manual_section = read_manual_section(os.path.join(root_path, 'context', 'status.md'))
    
    # 5. 生成当前时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 6. 构建 Markdown 内容
    tech_stack_md = ""
    if tech_stack:
        for tech, files in tech_stack.items():
            tech_stack_md += f"- **{tech}**"
            if tech in dependencies and dependencies[tech]:
                deps_str = ', '.join(dependencies[tech])
                tech_stack_md += f" (主要依赖: {deps_str})"
            tech_stack_md += f"\n  - 检测自: `{os.path.basename(files[0])}`\n"
    else:
        tech_stack_md = "_未检测到标准依赖文件_"
    
    content = f"""# 项目状态快照

> **⚠️ 注意**: 本文件由 `context/auto_status.py` 自动生成和维护  
> 请勿手动编辑 "自动生成区域"，可以编辑 "手动维护区域"

---

## 📊 自动生成区域

**生成时间**: {current_time}  
**项目规模**: {file_count} 个文件，{line_count:,} 行代码

### 技术栈
{tech_stack_md}

### 项目结构（最多 2 层深度）
```
{dir_structure}
```

---

## ✍️ 手动维护区域

{manual_section}

---

## 🔄 更新此文件

运行以下命令刷新自动生成的内容：

```bash
# Windows PowerShell
python context\\auto_status.py

# Linux/Mac
python3 context/auto_status.py
```

**推荐**：设置为 Git hooks 自动触发
```bash
# .git/hooks/post-commit
python context/auto_status.py
```
"""
    
    return content


def main():
    """主函数"""
    print("🔄 正在分析项目状态...")
    
    # 切换到项目根目录
    script_dir = Path(__file__).parent.parent
    os.chdir(script_dir)
    
    # 预先计算，避免重复调用
    tech_stack = detect_tech_stack('.')
    file_count, line_count = count_project_stats('.')
    
    # 生成内容（传入已计算的数据）
    content = generate_status_md('.')
    
    # 写入文件
    output_file = 'context/status.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 状态文件已更新: {output_file}")
    print("\n📋 摘要:")
    print(f"  - 文件数: {file_count}")
    print(f"  - 代码行数: {line_count:,}")
    print(f"  - 检测到技术栈: {', '.join(tech_stack.keys()) if tech_stack else '无'}")


if __name__ == '__main__':
    main()
