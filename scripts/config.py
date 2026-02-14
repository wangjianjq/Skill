"""
Centralized Configuration for Project Scripts
统一的项目脚本配置模块

用于消除代码重复 (DRY) 并统一路径处理逻辑。
"""

import os
from pathlib import Path

# --- 核心路径逻辑 ---
try:
    from scripts.utils import get_project_root, load_yaml_config
except ImportError:
    # 允许 config.py 被独立执行时的 fallback (虽然不建议)
    import sys
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    from scripts.utils import get_project_root, load_yaml_config

# 全局项目根目录
PROJECT_ROOT = get_project_root()

# --- 统一常量定义 ---

# 忽略的目录 (集合)
IGNORE_DIRS = {
    '.git', 
    '__pycache__', 
    'node_modules', 
    'context',       # context 目录通常包含生成的上下文，不作为源码扫描
    '.gemini', 
    '.history',
    '.idea',
    '.vscode',
    'dist',
    'build'
}

# 关注的文件扩展名 (集合)
EXTENSIONS = {
    '.py', '.md', '.json', '.js', '.ts', '.tsx', '.jsx', 
    '.vue', '.ps1', '.sh', '.txt', '.yaml', '.yml', '.toml'
}

# --- 动态加载核心文件列表 ---
def _load_core_files() -> set:
    """从 AGENTS_INDEX.yaml 加载核心文件列表，并合并基础默认值"""
    
    # 基础核心文件 (即便是 YAML 缺失也必须包含的)
    defaults = {
        'AGENTS.md', 'GEMINI.md', 'PROJECT_STATUS.md', 'README.md',
        'scripts/', '.agents/', 'context/'
    }
    
    yaml_path = PROJECT_ROOT / 'AGENTS_INDEX.yaml'
    if not yaml_path.exists():
        return defaults
        
    data = load_yaml_config(yaml_path)
    registry = data.get('registry', {})
    
    yaml_files = set()
    
    # 遍历 registry 下的所有部分 (context, languages, etc.)
    for section, items in registry.items():
        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict) and 'path' in item:
                    # 归一化路径：统一使用 /，并移除开头的 ./
                    raw_path = item['path'].replace('\\', '/')
                    if raw_path.startswith('./'):
                        raw_path = raw_path[2:]
                    yaml_files.add(raw_path)
                    
    return defaults.union(yaml_files)

CORE_FILES = _load_core_files()
