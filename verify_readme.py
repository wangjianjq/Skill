"""
README.md 完整验证脚本
检查文档结构、格式、链接完整性
"""
import re
from pathlib import Path

def main():
    readme_path = Path(__file__).parent / 'README.md'
    content = readme_path.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    print('=' * 80)
    print('📋 README.md 完整验证报告')
    print('=' * 80)
    print()
    
    # 1. 基本信息
    print('1️⃣ 文档基本信息')
    print(f'   总行数: {len(lines)}')
    print(f'   文件大小: {len(content):,} 字符')
    print()
    
    # 2. 检查emoji
    print('2️⃣ 章节标题 Emoji 检查')
    emoji_pattern = re.compile(r'[⭐🔧📁🧠🔴🟢🧪🤖📄🐙🧩📚🔒🎤🛡️📐🌍️]')
    headers_with_emoji = []
    for i, line in enumerate(lines, 1):
        if re.match(r'^#{1,6}\s+', line) and emoji_pattern.search(line):
            headers_with_emoji.append((i, line.strip()))
    
    if headers_with_emoji:
        print(f'   ❌ 发现 {len(headers_with_emoji)} 个包含 emoji 的标题:')
        for line_num, header in headers_with_emoji[:5]:
            print(f'      第{line_num}行: {header}')
    else:
        print('   ✅ 所有章节标题已清除 emoji')
    print()
    
    # 3. 目录树数量
    print('3️⃣ 目录树检查')
    tree_count = content.count('Agents-MD-Pro/')
    print(f'   找到 {tree_count} 个目录树')
    if tree_count == 2:
        print('   ✅ 正确(英文1个 + 中文1个)')
    else:
        print(f'   ⚠️  异常数量: {tree_count}')
    print()
    
    # 4. 文件分类章节
    print('4️⃣ "文件分类"章节检查')
    file_cat_en = len(re.findall(r'^### File Categories', content, re.MULTILINE))
    file_cat_cn = len(re.findall(r'^### 文件分类', content, re.MULTILINE))
    print(f'   英文 "File Categories": {file_cat_en} 个')
    print(f'   中文 "文件分类": {file_cat_cn} 个')
    if file_cat_en == 1 and file_cat_cn == 1:
        print('   ✅ 每个语言版本各1个')
    else:
        print('   ❌ 数量异常')
    print()
    
    # 5. 重复标题检查
    print('5️⃣ 重复章节检查')
    headers = re.findall(r'^#{1,6}\s+(.+)$', content, re.MULTILINE)
    header_counts = {}
    for h in headers:
        clean_h = h.strip()
        header_counts[clean_h] = header_counts.get(clean_h, 0) + 1
    
    duplicates = {h: c for h, c in header_counts.items() if c > 1}
    if duplicates:
        print(f'   ⚠️  发现 {len(duplicates)} 个重复标题:')
        for h, c in list(duplicates.items())[:3]:
            print(f'      "{h}" 出现 {c} 次')
    else:
        print('   ✅ 无重复章节标题')
    print()
    
    # 6. 目录链接验证
    print('6️⃣ 目录链接完整性检查')
    toc_section = re.search(r'## Table of Contents / 目录(.+?)(?=^##|\Z)', content, re.DOTALL | re.MULTILINE)
    if toc_section:
        toc_links = re.findall(r'\[(.+?)\]\(#(.+?)\)', toc_section.group(1))
        print(f'   目录链接数: {len(toc_links)}')
        
        # 提取所有实际标题并生成锚点
        actual_anchors = set()
        for match in re.finditer(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE):
            title = match.group(2).strip()
            # GitHub 锚点规则
            anchor = title.lower()
            anchor = re.sub(r'[^\w\s\u4e00-\u9fff-]', '', anchor)  # 移除特殊字符(保留中文)
            anchor = anchor.replace(' ', '-')
            actual_anchors.add(anchor)
        
        # 检查不匹配
        broken_links = []
        for text, anchor in toc_links:
            if anchor not in actual_anchors:
                broken_links.append((text, anchor))
        
        if broken_links:
            print(f'   ⚠️  发现 {len(broken_links)} 个无效链接:')
            for text, anchor in broken_links[:5]:
                print(f'      [{text}](#{anchor})')
        else:
            print('   ✅ 所有目录链接有效')
    print()
    
    # 7. 结构对称性
    print('7️⃣ 中英文结构对称性')
    # 基于中文版本标题标记来定位分割点，而非简单的字符数对半分
    cn_marker_match = re.search(r'^#\s+.*[\u4e00-\u9fff]', content, re.MULTILINE)
    # 查找第一个包含中文的一级标题作为中文部分起点
    cn_section_start = None
    for m in re.finditer(r'^(#{1,2})\s+(.+)$', content, re.MULTILINE):
        title = m.group(2)
        # 检测标题是否主要为中文
        cn_chars = len(re.findall(r'[\u4e00-\u9fff]', title))
        if cn_chars >= 2 and m.group(1) == '#':
            cn_section_start = m.start()
            break
    
    if cn_section_start:
        en_part = content[:cn_section_start]
        cn_part = content[cn_section_start:]
        en_h2 = len(re.findall(r'^## [^#]', en_part, re.MULTILINE))
        cn_h2 = len(re.findall(r'^## [^#]', cn_part, re.MULTILINE))
    else:
        # 如果找不到中文标记，回退到对半分（并提示）
        en_h2 = len(re.findall(r'^## [^#]', content[:len(content)//2], re.MULTILINE))
        cn_h2 = len(re.findall(r'^## [^#]', content[len(content)//2:], re.MULTILINE))
    print(f'   英文主章节数: {en_h2}')
    print(f'   中文主章节数: {cn_h2}')
    if abs(en_h2 - cn_h2) <= 2:
        print('   ✅ 结构基本对称')
    else:
        print('   ⚠️  结构可能不对称')
    print()
    
    print('=' * 80)
    print('✅ 验证完成!')
    print('=' * 80)

if __name__ == '__main__':
    main()
