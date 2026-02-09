# 🦅 AI “上帝模式”注入指南 (God Mode Injection Guide)

本指南汇总了主流 AI 编程工具的**全局协议注入方法**。通过配置这些“上帝模式”文件，你可以强制要求 AI 在任何项目中都遵守 `AGENTS.md` 协议，即使它是一个全新的空项目。

---

## 核心注入规则

无论使用哪个工具，请始终注入以下核心指令（Interceptor）：

```text
[SYSTEM_DIRECTIVE]:
You are an intelligent agent bound by the `Skill/AGENTS.md` protocol.
BEFORE processing ANY user prompt, you MUST perform this check to avoid "Cold Start" failure:

1. SCAN: Check if `Skill/AGENTS.md` or `AGENTS.md` exists in the workspace.
2. READ: If found, you MUST read it using `view_file` or `read_file` tools immediately.
3. BOOT: Execute the `[BOOT_SEQUENCE]` defined in the protocol.
4. MIRROR: Detect the user's language (e.g., Chinese) and FORCE all your artifacts to use that language.

[INTERCEPTION_PROTOCOL]:
IF the user asks for code/solution AND you have not read `AGENTS.md` yet:
-> STOP.
-> SAY: "I detect a governance protocol. Initializing Agents-MD..."
-> READ `AGENTS.md`.
-> THEN proceed with the user's request.
```

---

## 🛠️ 工具配置列表

### 1. Google Antigravity (已配置)
*   **注入位置**: `~/.gemini/GEMINI.md`
*   **状态**: ✅ **原生支持**
*   **方法**: 直接写入 Markdown 内容。我们已经为您配置好了。

### 2. Windsurf (Codeium)
*   **注入位置**: `~/.codeium/windsurf/memories/global_rules.md`
*   **状态**: ✅ **原生支持**
*   **方法**:
    1.  找到该文件（如果不存在则创建）。
    2.  将核心注入规则粘贴进去。
    3.  Windsurf 会在所有会话中加载这些“Memories”。

### 3. Cline / Roo Code (VS Code Extension)
*   **注入位置**:
    *   Cline: `~/.cline-rules` (或 `~/Documents/Cline/Rules`)
    *   Roo Code: `~/.roo/rules/global_rules.md` (推荐新建此文件)
*   **状态**: ✅ **原生支持**
*   **方法**:
    1.  在用户目录下创建对应文件。
    2.  粘贴规则。
    3.  Cline/Roo 会将这些作为 "Rule Bank" 或全局规则自动加载。

### 4. Cursor
*   **注入位置**: Cursor Settings -> General -> **Rules for AI**
*   **状态**: ⚠️ **仅通过 UI 配置** (无直接的上帝模式文件)
*   **方法**:
    1.  打开设置面板。
    2.  复制规则到 "Rules for AI" 文本框。
    3.  这是目前唯一的方法，Cursor 官方已弃用全局 `.cursorrules` 文件。

### 5. Claude Code (CLI)
*   **注入位置**: `~/.claude/CLAUDE.md`
*   **状态**: ✅ **原生支持 (推荐)**
*   **方法**:
    1.  在用户主目录 (`~/.claude/`) 下创建 `CLAUDE.md`。
    2.  写入核心注入规则。
    3.  Claude Code CLI 工具会自动读取此文件作为 Project/Global Context。

### 6. OpenAI ChatGPT (桌面版/网页版)
*   **注入位置**: Settings -> Personalization -> **Custom Instructions**
*   **状态**: ⚠️ **仅通过 UI 配置** (云端同步)
*   **方法**:
    1.  点击头像 -> Settings -> Personalization。
    2.  开启 "Custom Instructions"。
    3.  在 "How would you like ChatGPT to respond?" 中粘贴核心注入规则。
    4.  **注意**：此配置会同步到手机端和网页端。

### 7. Continue.dev
*   **注入位置**: `~/.continue/config.yaml`
*   **状态**: ⚙️ **需修改 YAML**
*   **方法**:
    在 `models` 配置中添加 `systemMessage`：
    ```yaml
    models:
      - title: GPT-4o
        provider: openai
        model: gpt-4o
        systemMessage: |
           [粘贴核心注入规则]
    ```

### 8. Aider (CLI)
*   **注入位置**: 启动参数或环境变量
*   **状态**: ❌ **困难** (无纯文本全局提示词文件)
*   **方法**:
    Aider 更倾向于通过 `--message` 或 `--chat-language` 控制。最接近的方法是创建一个别名 (Alias) 来启动 Aider：
    `alias aider='aider --system-prompt "Skill/AI_RULES_INJECTION.txt"'` (需要指向一个具体存在的路径)

### 9. Google Gemini CLI (`@google/gemini-cli`)
*   **注入位置**: 环境变量 `GEMINI_SYSTEM_MD`
*   **状态**: ✅ **原生支持 (极强)**
*   **方法**:
    1.  创建一个包含核心注入规则的文件，例如 `~/.gemini/global_system.md`。
    2.  设置环境变量（建议写入 Shell 配置文件如 `.zshrc` 或 `.bashrc`）：
        `export GEMINI_SYSTEM_MD="/path/to/your/global_system.md"`
    3.  重启终端。Gemini CLI 启动时会强制使用该文件内容作为 System Prompt。

---

## 🎯 最佳实践建议

1.  **Antigravity, Windsurf, Cline/Roo** 是支持度最好的工具，因为它们允许**文件级**的全局上下文注入。
2.  **Claude Code** 和 **Gemini CLI** 是命令行工具中的王者，支持完美的文件注入。
3.  对于 **Cursor**，必须手动在每台机器的设置里粘贴一次。
