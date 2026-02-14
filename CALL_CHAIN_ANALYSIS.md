# 上下文注入系统架构分析 (v8.0)

## 1. 系统概述

本项目采用**混合上下文注入系统 (Hybrid Context Injection System)**，旨在解决大模型在长对话中的"遗忘"与"幻觉"问题。

### 核心组件

1.  **`make_prompt.py` (动态上下文构建器)**
    - **作用**: 为不支持自动加载的 AI (如 Claude/ChatGPT 网页版) 生成"三明治提示词"。
    - **机制**: 组合 `context/memory.md` (长期记忆) + `context/status.md` (实时状态) + 用户问题。
    - **分层策略**:
        - 小型项目 (<100文件): 完整目录树
        - 中型项目 (<300文件): 2层深度
        - 大型项目 (>300文件): 1层深度

2.  **`context/status.md` (项目状态快照)**
    - **作用**: 存储项目当前的实际结构、技术栈和统计信息。
    - **特性**: 被动更新，作为 AI 的"短期记忆"。

3.  **`context/auto_status.py` (状态维护工具)**
    - **作用**: 扫描项目并更新 `status.md`。
    - **触发**: 推荐通过 Git Hook (post-commit) 自动触发。

## 2. 调用链分析

### A. 主动调用 (Active Invocation)
由用户手动执行，适用于高精度需求。

```bash
python make_prompt.py "你的问题"
```

### B. 被动加载 (Passive Loading)
由 AI 工具通过适配器自动读取。

- **Gemini CLI**: 通过 `GEMINI.md` (需配置) 或 `AGENTS.md` (v8.0SSOT) 读取。
- **IDE (Cursor/Windsurf/VSCode)**: 通过 `.cursorrules`, `.windsurfrules` 等规则文件引导读取 `AGENTS.md`。

## 3. 依赖关系图

```mermaid
graph TD
    User[用户] -->|运行| MakePrompt[make_prompt.py]
    User -->|运行| AutoStatus[context/auto_status.py]
    AutoStatus -->|写入| StatusMD[context/status.md]
    
    MakePrompt -->|读取| Memory[context/memory.md]
    MakePrompt -->|读取| StatusMD
    MakePrompt -->|生成| Prompt[三明治 Prompt]
    
    AI_Agent[AI Agent] -->|读取 (v8.0)| AgentsMD[AGENTS.md]
    AI_Agent -->|被动感知| StatusMD
```

## 4. 维护策略 (v8.0)

- **保留**: `make_prompt.py`, `context/status.md`, `context/auto_status.py` 是核心组件，**必须保留**。
- **废弃**: 旧版的 `scan_results.txt` (已由 `status.md` 取代)。
- **修复**: 确保 `GEMINI.md` 等适配器文件包含对 `AGENTS.md` 的引用。
