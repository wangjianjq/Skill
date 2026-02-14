"""
README.md 链接验证脚本
验证所有目录链接是否正确指向对应的章节标题
"""
import re
import sys
import os
from pathlib import Path

# 确保可以导入项目中的模块
project_root = Path(__file__).parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

def extract_toc_links(content):
    """提取目录中的所有链接"""
    # 匹配形如 [文本](#锚点) 的链接
    pattern = r'\[([^\]]+)\]\(#([^\)]+)\)'
    return re.findall(pattern, content)

def extract_headers(content):
    """提取所有章节标题及其锚点"""
    headers = {}
    prefix_map = {}  # 优化：用于快速模糊匹配的辅助索引
    lines = content.split('\n')
    
    # 动态加载隐藏目录中的工具
    import importlib.util
    utils_path = project_root / '.agents' / 'skills' / 'shared-utils' / 'markdown_utils.py'
    spec = importlib.util.spec_from_file_location("markdown_utils", utils_path)
    markdown_utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(markdown_utils)
    generate_github_anchor = markdown_utils.generate_github_anchor
    
    for line in lines:
        match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if match:
            title = match.group(2).strip()
            anchor = generate_github_anchor(title)
            headers[anchor] = {'title': title, 'line': line}
            
            # 建立前缀索引 (取前10个字符)
            prefix = anchor[:10]
            if prefix not in prefix_map:
                prefix_map[prefix] = []
            prefix_map[prefix].append(anchor)
    
    return headers, prefix_map

def verify_readme_links(readme_path, output_file=None):
    """验证 README 文件的链接"""
    def output(msg):
        if output_file:
            output_file.write(msg + '\n')
        else:
            print(msg)
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    toc_links = extract_toc_links(content)
    output(f"[TOC] 找到 {len(toc_links)} 个目录链接")
    
    headers, prefix_map = extract_headers(content)
    output(f"[HEADERS] 找到 {len(headers)} 个章节标题\n")
    
    invalid_links = []
    valid_links = []
    
    for link_text, anchor in toc_links:
        if anchor in headers:
            valid_links.append((link_text, anchor, headers[anchor]['title']))
        else:
            invalid_links.append((link_text, anchor))
    
    if invalid_links:
        output("[ERROR] 发现失效链接:\n")
        for text, anchor in invalid_links:
            output(f"  链接: [{text}](#{anchor})")
            output(f"  问题: 未找到对应的章节标题")
            
            # 使用前缀索引进行快速模糊搜索 (O(1) 索引查找)
            similar = prefix_map.get(anchor[:10], [])
            if similar:
                output(f"  建议: 可能的目标 -> {similar[:3]}")
            output('')
    else:
        output("[OK] 所有目录链接均有效!\n")
    
    output(f"总计: {len(valid_links)} 个有效链接, {len(invalid_links)} 个失效链接")
    
    # 显示前10个有效链接作为示例
    if valid_links:
        output("\n[SAMPLE] 有效链接示例 (前10个):")
        for i, (text, anchor, title) in enumerate(valid_links[:10], 1):
            output(f"  {i}. [{text}](#{anchor}) -> {title}")
    
    return len(invalid_links) == 0

if __name__ == "__main__":
    project_root = Path(__file__).parent
    readme_path = project_root / 'README.md'
    output_path = project_root / 'link_verification_report.txt'
    
    if not readme_path.exists():
        print(f"文件不存在: {readme_path}")
        exit(1)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + '\n')
        f.write(" README.md 链接验证\n")
        f.write("=" * 60 + '\n\n')
        
        success = verify_readme_links(readme_path, f)
        
        f.write('\n')
        f.write("=" * 60 + '\n')
        if success:
            f.write("验证通过!\n")
        else:
            f.write("发现问题,请修复失效链接\n")
        f.write("=" * 60 + '\n')
    
    print(f"验证报告已生成: {output_path}")
    
    # 打印报告内容
    with open(output_path, 'r', encoding='utf-8') as f:
        print(f.read())
    
    exit(0 if success else 1)
