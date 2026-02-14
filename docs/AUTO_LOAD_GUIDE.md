# 自动加载配置指南 (Auto-Load Guide)

为了解决 AI 忽略 `AGENTS.md` 的问题，我们需要在 IDE 层面进行**一次性配置**。这将确保所有的 AI 交互都自动遵守协议。

## 1. 获取注入规则

请打开项目根目录下的文件：
`Skill/AI_RULES_INJECTION.txt`

复制其中的全部内容。

## 2. 配置您的 IDE

### A. Cursor (推荐)

1.  按 `Ctrl+Shift+P` (Windows) 或 `Cmd+Shift+P` (Mac)。
2.  输入 `Cursor: Open Settings` 并回车。
3.  找到 **General** -> **Rules for AI** (或者在最新的版本中可能是 **Project Rules**)。
4.  将内容粘贴进去。
5.  保存。

### B. VS Code + Copilot

1.  打开设置 (Settings)。
2.  搜索 `Copilot: Custom Instructions`。
3.  在 `Edit in settings.json` 或文本框中，粘贴内容。
    *   注意：Copilot 的指令长度限制较严格，如果太长，可以只粘贴 `[SYSTEM_DIRECTIVE]` 部分。

### C. Windsurf

1.  在侧边栏找到 Cascade (AI 对话框)。
2.  点击设置图标或寻找 `Personal Rules` / `Memories`。
3.  粘贴规则内容。

---

## 3. 验证生效

1.  开启一个新的对话窗口。
2.  直接提问：“写一个 Python Hello World”。
3.  **预期行为**：
    *   AI **不会** 直接写代码。
    *   AI 会说：“我检测到了 `Skill/AGENTS.md`，正在初始化协议...”
    *   AI 会自动读取 `AGENTS.md`。
    *   AI 会用**中文**回复后续计划（因为规则里强调了 `MIRROR`）。

> **原理**：我们将规则注入到了 System Prompt 层级，这是 AI 最无法忽略的指令区域。
