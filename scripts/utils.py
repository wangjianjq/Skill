"""
Shared Utility Functions
共享工具库

提供路径解析、YAML 读取等通用功能。
旨在无第三方依赖运行 (Zero-Dependency).
"""

import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Union

def get_project_root() -> Path:
    """
    动态查找项目根目录。
    逻辑：
    1. 检查环境变量 'AGENTS_PROJECT_ROOT'
    2. 向上查找包含 'AGENTS.md' 的目录 (最多 5 层)
    3. Fallback: 假设脚本在 scripts/utils.py，返回 ../../
    """
    # 1. Environment Variable
    env_root = os.environ.get('AGENTS_PROJECT_ROOT')
    if env_root and os.path.exists(env_root):
        return Path(env_root).resolve()

    # 2. Upward Search
    current = Path(__file__).resolve().parent
    for _ in range(5):
        if (current / "AGENTS.md").exists():
            return current
        if current.parent == current: # Reached filesystem root
            break
        current = current.parent
    
    # 3. Fallback (Relative to this file: scripts/utils.py -> project_root)
    # scripts/utils.py -> scripts/ -> project_root
    return Path(__file__).resolve().parent.parent

class SimpleYamlParser:
    """
    一个极简的 YAML 解析器，用于在没有 PyYAML 依赖的环境中读取 AGENTS_INDEX.yaml。
    *仅支持本项目使用的 YAML 及其简单子集。*
    """
    
    @staticmethod
    def parse(file_path: Union[str, Path]) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        result = {}
        stack = [(result, -1)]  # (current_dict_or_list, indentation_level)
        
        # 极其简化的解析逻辑，仅为了读取核心配置
        # 实际生产建议在环境准备好后使用 pip install pyyaml
        # 这里仅作 fallback 或简单读取
        
        # 为了安全和简单，针对 AGENTS_INDEX.yaml 的特定结构进行硬编码解析可能更稳健
        # 但我们尝试做一个稍微通用的简单解析
        
        # 警告：这是一个非常脆弱的解析器，仅用于 demo 或简单场景
        # 对于 AGENTS_INDEX.yaml 的 registry 部分，我们主要关心 list 和 dict
        return SimpleYamlParser._heuristic_parse(lines)

    @staticmethod
    def _heuristic_parse(lines: List[str]) -> Dict[str, Any]:
        """
        针对 AGENTS_INDEX.yaml 结构的启发式解析。
        只提取 registry 下的 path 信息。
        """
        data = {'registry': {}}
        current_section = None
        
        for line in lines:
            line = line.rstrip()
            if not line or line.strip().startswith('#'):
                continue
                
            indent = len(line) - len(line.lstrip())
            content = line.strip()
            
            # print(f"DEBUG PARSE: indent={indent} content='{content}'")
            
            # Top level keys
            if indent == 0 and content.endswith(':'):
                key = content[:-1]
                if key == 'registry':
                    pass # We are in registry
                else:
                    current_section = None # Ignore other sections
                    
            # Registry sections (context, languages, etc.)
            elif indent == 2 and content.endswith(':'):
                current_section = content[:-1]
                if current_section not in data['registry']:
                     data['registry'][current_section] = []
            
            # List items or properties
            elif indent >= 4:
                if current_section:
                    # 尝试提取 path
                    if 'path:' in content:
                        # 分割 'path:' 并获取右侧部分
                        parts = content.split('path:')
                        if len(parts) > 1:
                            path_part = parts[1]
                            
                            # 清理可能存在的尾部注释
                            if '#' in path_part:
                                path_part = path_part.split('#')[0]
                            
                            # 清理逗号和花括号 (针对 inline dicts)
                            path_part = path_part.split(',')[0].strip().rstrip('}').strip()
                            
                            # 清理引号
                            path_part = path_part.strip('"\'')
                            
                            if path_part:
                                data['registry'][current_section].append({'path': path_part})
        
        return data

def load_yaml_config(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    尝试加载 YAML 文件。
    优先使用 PyYAML，如果不存在则使用内置简单解析器。
    """
    try:
        import yaml
        print(f"DEBUG: Using PyYAML to load {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except ImportError:
        print("DEBUG: PyYAML not found, using SimpleYamlParser.")
        return SimpleYamlParser.parse(file_path)
    except Exception as e:
        print(f"⚠️ Error loading YAML {file_path}: {e}")
        return {}
