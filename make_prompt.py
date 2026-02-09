import os
import datetime
import sys

# --- 配置 ---
IGNORE_DIRS = {'.git', '__pycache__', 'node_modules', 'context', '.gemini', '.history'}
EXTENSIONS = {'.py', '.md', '.json', '.js', '.vue', '.ps1', '.sh', '.txt'}

# --- 项目规模阈值（用于分层策略）---
MAX_FILES_FULL_TREE = 100      # 小型项目：完整树
MAX_FILES_TRUNCATED = 300      # 中型项目：截断到 2 层深度
# 超过 300 文件：仅显示根目录和一级子目录

def get_tree_structure(startpath):
    """自动生成项目目录树，根据项目规模动态调整深度，避免超长上下文"""
    
    # 步骤 1: 快速统计文件数
    file_count = 0
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        file_count += sum(1 for f in files if any(f.endswith(ext) for ext in EXTENSIONS))
    
    # 步骤 2: 根据规模决定深度策略
    if file_count <= MAX_FILES_FULL_TREE:
        depth_limit = None  # 完整树
        strategy = "完整树"
    elif file_count <= MAX_FILES_TRUNCATED:
        depth_limit = 2
        strategy = "2层深度"
    else:
        depth_limit = 1
        strategy = "1层深度（大型项目）"
    
    # 步骤 3: 生成树结构
    tree_str = f"Project Structure (📊 {file_count} 个文件，策略: {strategy}):\n"
    
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        # 计算当前深度
        level = root.replace(startpath, '').count(os.sep)
        
        # 应用深度限制
        if depth_limit is not None and level >= depth_limit:
            dirs[:] = []  # 不再深入子目录
            if level > depth_limit:
                continue
        
        indent = ' ' * 4 * level
        tree_str += f"{indent}{os.path.basename(root)}/\n"
        
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if any(f.endswith(ext) for ext in EXTENSIONS):
                tree_str += f"{subindent}{f}\n"
    
    return tree_str

def read_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def generate_prompt(user_query):
    # 1. 获取实时数据
    tree = get_tree_structure(".")
    status = read_file("context/status.md")
    memory = read_file("context/memory.md")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # 2. 构建"三明治" Prompt (核心融合点)
    # 顺序：用户问题(首因) -> 静态记忆 -> 动态状态 -> 重复问题(近因)
    final_prompt = f"""
---
[SYSTEM INSTRUCTION]: 
You are an expert developer. Answer the question based strictly on the context below.

[User Query Summary]: 
"{user_query}"

[Layer 1: Long-term Memory (ADR Logs)]:
{memory}

[Layer 2: Current Project State (RAM)]:
<current_time>{current_time}</current_time>
{status}
<file_tree>
{tree}
</file_tree>

[Instruction]: 
Answer the user's question now. 
1. Check the 'Long-term Memory' for constraints (e.g., banned functions).
2. Check the 'file_tree' to understand where files are located.
3. If you write code, ensure it matches the 'status' (Tech Stack).

[User Query]: 
"{user_query}"
---
"""
    return final_prompt

if __name__ == "__main__":
    # check if interactive mode (no args)
    if len(sys.argv) > 1:
        # One-shot mode
        query = " ".join(sys.argv[1:])
        prompt = generate_prompt(query)
        try:
            import pyperclip
            pyperclip.copy(prompt)
            print("\n✅ Prompt 已复制到剪贴板！(One-shot)")
        except ImportError:
            print(prompt)
    else:
        # Interactive Mode (REPL)
        print("="*60)
        print("🧠 DCIP Console: 动态上下文注入控制台")
        print("   (输入 'q' 或 'exit' 退出)")
        print("="*60)
        
        try:
            import pyperclip
            HAS_CLIPBOARD = True
        except ImportError:
            HAS_CLIPBOARD = False
            print("⚠️ [Info] 未检测到 pyperclip 模块。")
            print("   (将仅在屏幕显示 Prompt。建议安装: pip install pyperclip)")

        while True:
            try:
                query = input("\n[DCIP] 请输入你的问题: ").strip()
                if query.lower() in ('q', 'exit', 'quit'):
                    print("Bye!")
                    break
                if not query:
                    continue
                    
                prompt = generate_prompt(query)
                
                if HAS_CLIPBOARD:
                    try:
                        pyperclip.copy(prompt)
                        print("✅ Prompt 已复制！(粘贴给 AI 即可)")
                    except Exception as e:
                        print(f"⚠️ 复制失败: {e}")
                        print(prompt)
                else:
                    print("-" * 40)
                    print(prompt)
                    print("-" * 40)
                    print("📋 请手动复制上方内容")
                    
            except KeyboardInterrupt:
                print("\nBye!")
                break
            except Exception as e:
                print(f"Error: {e}")
