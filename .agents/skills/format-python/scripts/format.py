#!/usr/bin/env python3
"""
format-python Skill - 跨平台 Python 实现

使用 skill_wrapper 框架实现的 Black 代码格式化器
"""

import sys
from pathlib import Path

# 添加 _shared 到模块路径（向上两级到 skills，然后进入 _shared）
_shared_dir = Path(__file__).parent.parent.parent / '_shared'
sys.path.insert(0, str(_shared_dir))

from skill_wrapper import SkillRunner


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Python 代码格式化 (Black)',
        epilog='示例: python format.py . --check'
    )
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='要格式化的目标路径（默认: 当前目录）'
    )
    parser.add_argument(
        '--check',
        action='store_true',
        help='检查模式: 仅检查不修改文件'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='详细输出'
    )
    
    args = parser.parse_args()
    
    # 创建并运行 Skill
    runner = SkillRunner(
        skill_name='format-python',
        tool_command=['black', '{path}'],
        check_command=['black', '--version']
    )
    
    exit_code = runner.run(
        path=args.path,
        check_mode=args.check,
        verbose=args.verbose
    )
    
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
