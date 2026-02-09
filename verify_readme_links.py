"""
README.md 链接验证脚本
验证所有目录链接是否正确指向对应的章节标题
"""
import re
from pathlib import Path

def extract_toc_links(content):
    """提取目录中的所有链接"""
    # 匹配形如 [文本](#锚点) 的链接
    pattern = r'\[([^\]]+)\]\(#([^\)]+)\)'
    return re.findall(pattern, content)

def extract_headers(content):
    """提取所有章节标题及其锚点"""
    headers = {}
    lines = content.split('\n')
    
    for line in lines:
        # 匹配 Markdown 标题
        match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            # 生成锚点(简化版,根据 GitHub 规则)
            anchor = title.lower()
            # 移除特殊字符,保留中文、字母、数字、空格和连字符
            anchor = re.sub(r'[^\w\s\u4e00-\u9fff-]', '', anchor)
            # 将空格替换为连字符
            anchor = re.sub(r'\s+', '-', anchor)
            headers[anchor] = {'title': title, 'level': level, 'line': line}
    
    return headers

def verify_readme_links(readme_path, output_file=None):
    """验证 README 文件的链接"""
    def output(msg):
        if output_file:
            output_file.write(msg + '\n')
        else:
            print(msg)
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取目录链接
    toc_links = extract_toc_links(content)
    output(f"[TOC] 找到 {len(toc_links)} 个目录链接")
    
    # 提取章节标题
    headers = extract_headers(content)
    output(f"[HEADERS] 找到 {len(headers)} 个章节标题\n")
    
    # 验证链接
    invalid_links = []
    valid_links = []
    
    for link_text, anchor in toc_links:
        if anchor in headers:
            valid_links.append((link_text, anchor, headers[anchor]['title']))
        else:
            invalid_links.append((link_text, anchor))
    
    # 输出结果
    if invalid_links:
        output("[ERROR] 发现失效链接:\n")
        for text, anchor in invalid_links:
            output(f"  链接: [{text}](#{anchor})")
            output(f"  问题: 未找到对应的章节标题")
            # 查找相似的标题
            similar = [h for h in headers.keys() if anchor[:10] in h or h[:10] in anchor]
            if similar:
                output(f"  建议: 可能的目标 -> {similar[:3]}")
            output('')
    else:
        output("[OK] 所有目录链接均有效!\n")
    
    output(f"总计: {len(valid_links)} 个有效链接, {len(invalid_links)} 个失效链接")
    
    # 显示前10个有效链接作为示例
    if valid_links:
        output("\\n[SAMPLE] 有效链接示例 (前10个):")
        for i, (text, anchor, title) in enumerate(valid_links[:10], 1):
            output(f"  {i}. [{text}](#{anchor}) -> {title}")
    
    return len(invalid_links) == 0

if __name__ == "__main__":
    readme_path = Path(r"c:\Users\WJ\Desktop\Skill\README.md")
    output_path = Path(r"c:\Users\WJ\Desktop\Skill\link_verification_report.txt")
    
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
