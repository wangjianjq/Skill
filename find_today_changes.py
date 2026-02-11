#!/usr/bin/env python3
"""
遍历项目目录，找出今天修改的文件
"""

import os
from datetime import datetime, date
from pathlib import Path

# 忽略的目录
IGNORE_DIRS = {'.git', '__pycache__', 'node_modules', '.gemini', '.history', '.idea', '.vscode'}

def get_modified_files_today(root_path='.'):
    """获取今天修改的文件"""
    today = date.today()
    modified_files = []
    
    for root, dirs, files in os.walk(root_path):
        # 过滤忽略目录
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # 获取文件修改时间
                mtime = os.path.getmtime(file_path)
                mtime_date = datetime.fromtimestamp(mtime).date()
                
                # 检查是否今天修改
                if mtime_date == today:
                    # 获取文件大小
                    size = os.path.getsize(file_path)
                    # 获取修改时间（精确到分钟）
                    mtime_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
                    
                    modified_files.append({
                        'path': os.path.relpath(file_path, root_path),
                        'size': size,
                        'mtime': mtime_str,
                        'mtime_ts': mtime
                    })
            except (OSError, PermissionError):
                # 跳过无法访问的文件
                pass
    
    # 按修改时间排序
    modified_files.sort(key=lambda x: x['mtime_ts'])
    return modified_files


def format_size(size_bytes):
    """格式化文件大小"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


def main():
    print("🔍 正在遍历项目目录...")
    print(f"📅 查找日期: {date.today()}")
    print("")
    
    files = get_modified_files_today('.')
    
    if not files:
        print("❌ 未找到今天修改的文件")
        return
    
    print(f"✅ 找到 {len(files)} 个今天修改的文件:\n")
    print("-" * 80)
    print(f"{'修改时间':<20} {'大小':<12} {'文件路径'}")
    print("-" * 80)
    
    # 按类别分组
    new_files = []
    modified_files = []
    
    for f in files:
        print(f"{f['mtime']:<20} {format_size(f['size']):<12} {f['path']}")
        
        # 通过创建时间与修改时间判断：如果创建时间也是今天，则为新增文件
        file_path = os.path.join('.', f['path'])
        try:
            ctime = os.path.getctime(file_path)
            ctime_date = datetime.fromtimestamp(ctime).date()
            if ctime_date == date.today():
                new_files.append(f['path'])
            else:
                modified_files.append(f['path'])
        except (OSError, PermissionError):
            modified_files.append(f['path'])
    
    print("-" * 80)
    print(f"\n📊 统计:")
    print(f"  - 总文件数: {len(files)}")
    print(f"  - 总大小: {format_size(sum(f['size'] for f in files))}")
    
    # 分类统计
    if new_files:
        print(f"\n🆕 新增文件 ({len(new_files)}):")
        for path in new_files:
            print(f"  - {path}")
    
    if modified_files:
        print(f"\n🔄 修改文件 ({len(modified_files)}):")
        for path in modified_files:
            print(f"  - {path}")


if __name__ == '__main__':
    main()
