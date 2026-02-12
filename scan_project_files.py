#!/usr/bin/env python3
"""
识别项目中的临时文件、垃圾文件和与引导系统无关的文件
"""

import os

# 临时文件模式
TEMP_PATTERNS = {
    # Python
    '*.pyc', '*.pyo', '*.pyd', '__pycache__',
    # 编辑器/IDE
    '*.swp', '*.swo', '*~', '.DS_Store', 'Thumbs.db',
    '*.tmp', '*.temp', '*.bak', '*.cache',
    # 构建产物
    'dist/', 'build/', '*.egg-info/', '.eggs/',
    # Node
    'node_modules/', 'package-lock.json', 'yarn.lock',
    # 日志
    '*.log', 'logs/',
    # Git
    '.git/',
}

# 项目引导/索引文件（核心文件）
CORE_FILES = {
    # 主引导文件
    'AGENTS.md', 'GEMINI.md', 'CLAUDE.md', 'CONVENTIONS.md',
    'PROJECT_STATUS.md', 'PROJECT_GOVERNANCE.md',
    'CHANGELOG.md', 'README.md',
    
    # 配置目录
    '.agents/', '.claude/', '.codex/', '.github/', '.idea/', '.zed/',
    'bmad/', 'docs/',
    
    # Context 系统
    'context/', 'make_prompt.py',
    
    # Skills 核心
    '.agents/skills/',
    
    # 工具脚本
    'setup.bat', 'setup.sh', 'ResetAG.bat', 'ResetAG.sh',
}

IGNORE_DIRS = {'.git', '__pycache__', 'node_modules', '.gemini', '.history'}

def matches_pattern(path, pattern):
    """检查路径是否匹配模式"""
    # 统一使用 / 分隔符
    normalized = path.replace(os.sep, '/')
    parts = normalized.split('/')
    basename = parts[-1] if parts else ''
    
    if pattern.endswith('/'):
        # 目录模式：支持精确目录名与通配符目录名
        dir_name = pattern[:-1]
        if '*' in dir_name:
            suffix = dir_name.split('*')[-1]
            return any(part.endswith(suffix) for part in parts[:-1])
        return dir_name in parts[:-1]  # 只检查目录部分
    elif '*' in pattern:
        # 通配符模式：只匹配文件扩展名
        ext = pattern.split('*')[-1]
        return basename.endswith(ext)
    else:
        # 完整文件名匹配
        return basename == pattern

def is_temp_file(path):
    """判断是否为临时文件"""
    for pattern in TEMP_PATTERNS:
        if matches_pattern(path, pattern):
            return True
    return False

def is_core_file(rel_path):
    """判断是否为核心引导文件"""
    # 统一使用 / 分隔符，兼容 Windows
    normalized = rel_path.replace(os.sep, '/')
    
    # 检查完整路径（精确匹配文件名）
    if normalized in CORE_FILES:
        return True
    
    # 检查是否在核心目录下
    for core in CORE_FILES:
        if core.endswith('/') and normalized.startswith(core):
            return True
    
    return False

def scan_project(root_path='.'):
    """扫描项目文件"""
    temp_files = []
    non_core_files = []
    all_files = []
    
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, root_path)
            
            try:
                size = os.path.getsize(file_path)
                
                is_temp = is_temp_file(rel_path)
                is_core = is_core_file(rel_path)

                all_files.append({
                    'path': rel_path,
                    'size': size,
                    'is_temp': is_temp,
                    'is_core': is_core
                })

                if is_temp:
                    temp_files.append({'path': rel_path, 'size': size})
                elif not is_core:
                    non_core_files.append({'path': rel_path, 'size': size})
                    
            except (OSError, PermissionError):
                pass
    
    return temp_files, non_core_files, all_files

def format_size(size_bytes):
    """格式化文件大小"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"

def main():
    print("Scanning project files...")
    print("")
    
    temp_files, non_core_files, all_files = scan_project('.')
    
    # 统计
    total_size = sum(f['size'] for f in all_files)
    temp_size = sum(f['size'] for f in temp_files)
    non_core_size = sum(f['size'] for f in non_core_files)
    core_files = [f for f in all_files if f['is_core'] and not f['is_temp']]
    core_size = sum(f['size'] for f in core_files)
    
    print("=" * 80)
    print("PROJECT FILE CLASSIFICATION")
    print("=" * 80)
    print(f"Total files: {len(all_files)}")
    print(f"Total size: {format_size(total_size)}")
    print("")
    print(f"Core files: {len(core_files)} files ({format_size(core_size)})")
    print(f"Temp/Junk files: {len(temp_files)} files ({format_size(temp_size)})")
    print(f"Non-core files: {len(non_core_files)} files ({format_size(non_core_size)})")
    print("=" * 80)
    
    # 临时文件详情
    if temp_files:
        print("\nTEMP/JUNK FILES:")
        print("-" * 80)
        for f in sorted(temp_files, key=lambda x: x['size'], reverse=True):
            print(f"  {format_size(f['size']):>10}  {f['path']}")
        print("-" * 80)
        print(f"TIP: Safe to delete, saves {format_size(temp_size)}")
    
    # 非核心文件详情
    if non_core_files:
        print("\nNON-CORE FILES (unrelated to index/guide system):")
        print("-" * 80)
        
        # 按目录分组
        by_dir = {}
        for f in non_core_files:
            dir_name = os.path.dirname(f['path']) or 'ROOT'
            if dir_name not in by_dir:
                by_dir[dir_name] = []
            by_dir[dir_name].append(f)
        
        for dir_name, files in sorted(by_dir.items()):
            dir_size = sum(f['size'] for f in files)
            print(f"\n[{dir_name}] ({len(files)} files, {format_size(dir_size)}):")
            for f in sorted(files, key=lambda x: x['size'], reverse=True)[:10]:
                print(f"  {format_size(f['size']):>10}  {os.path.basename(f['path'])}")
            if len(files) > 10:
                print(f"  ... and {len(files) - 10} more files")
        
        print("-" * 80)
        print("NOTE: These may be test files, examples, or auxiliary files.")
        print("      Review before deleting.")

if __name__ == '__main__':
    main()
