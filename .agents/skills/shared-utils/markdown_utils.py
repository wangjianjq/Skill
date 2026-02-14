import re

def generate_github_anchor(title: str) -> str:
    """
    统一的 GitHub 风格锚点生成算法
    规则:
    1. 转小写
    2. 移除特殊字符（保留中文、字母、数字、空格、连字符）
    3. 将所有空白字符（空格、制表符等）替换为单个连字符
    """
    # 1. 转小写
    anchor = title.lower()
    # 2. 移除特殊字符 (保留中文、字母、数字、空格、连字符)
    anchor = re.sub(r'[^\w\s\u4e00-\u9fff-]', '', anchor)
    # 3. 将所有空白字符替换为连字符
    anchor = re.sub(r'\s+', '-', anchor)
    # 4. 去除两端的连字符
    anchor = anchor.strip('-')
    return anchor
