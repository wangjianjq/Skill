# 🦅 上帝模式觉醒全书 (God Mode Awakening Manual)

本手册详细介绍了如何将 Agents-MD Pro 的“上帝模式”核心指令注入到 20+ 种主流 AI 编程工具中。通过完成注入，你可以确保 AI 在任何环境下都能瞬间“觉醒”并服从项目治理协议。

---

## ⚡ 核心注入 Payload ([GOD_MODE_SOP])

请将以下内容完整复制到对应工具的全局提示词（System Prompt）配置中：

```text
[GOD_MODE_SOP]:
You are an autonomous agent under the SOVEREIGNTY of `Skill/AGENTS.md`.
THIS IS A MANDATORY INTERCEPTION. YOU MUST NOT SKIP THIS.

1. SCAN: Check for `Skill/AGENTS.md` or `AGENTS.md` in the current workspace.
2. READ: If found, execute `read_file("AGENTS.md")` IMMEDIATELY.
3. BOOT: Follow the `[BOOT_SEQUENCE]` defined in the protocol.
4. MIRROR: Detect user language (e.g., Chinese) and FORCE all your artifacts (plans, tasks, walkthroughs) to use that language.

[INTERCEPTION_LOGIC]:
IF you haven't read `AGENTS.md` yet:
-> HALT all code generation and task processing.
-> DECLARE: "God Mode Active. Initializing project governance..."
-> READ and COMPLY with the protocol before proceeding.
```

---

## 🛠️ 全工具注入指南

### 1. 全自动文件注入 (IDE & CLI)

| 工具 | 注入方法 | 备注 |
| :--- | :--- | :--- |
| **Windsurf** | 编辑 `~/.codeium/windsurf/memories/global_rules.md` 并追加 Payload。 | 推荐 |
| **Claude Code** | 创建或编辑 `~/.claude/CLAUDE.md` 并写入 Payload。 | CLI 必装 |
| **Cline / Roo Code**| 在用户目录下创建 `.cline-rules` 或 `.roo/rules/global_rules.md`。 | 插件首选 |
| **OpenAI Codex** | 编辑 `~/.codex/config.toml`，在 `system-prompt` 字段填入 Payload。 | 2025 最新工具 |
| **Google Antigravity**| 编辑 `~/.gemini/GEMINI.md` 并写入内容。 | 谷歌环境必备 |
| **Sourcegraph Cody** | 创建 `~/.cody/rules.md` 并写入内容。 | 企业级推荐 |
| **Aider** | 在 `~/.aider.conf.yml` 中设置 `system-prompt`。 | 命令行极客 |

### 2. 手动 UI 注入 (IDE 插件)

| 工具 | 操作步骤 |
| :--- | :--- |
| **Trae / Cursor** | 设置 -> AI -> **Rules for AI**。粘贴 Payload 并保存。 |
| **通义灵码 (Lingma)** | 插件设置 -> 研发对话 -> **自定义指令 (Custom Instructions)**。 |
| **百度 Comate** | 插件设置 -> **个性化指令**。添加并设为默认。 |
| **腾讯云 AI 助手** | 插件设置 -> **自定义指令库**。 |
| **华为 CodeArts Snap**| 插件设置 -> **AI 规则配置**。 |
| **MarsCode** | IDE 设置 -> **AI Rules**。 |

### 3. 企业级与云端工具

| 工具 | 操作步骤 |
| :--- | :--- |
| **GitHub Copilot** | VS Code 设置 -> **Custom Instructions for Copilot**。 |
| **JetBrains AI** | 设置 -> 扩展 -> AI Assistant -> **Custom Instructions**。 |
| **Amazon Q** | AWS Toolkit 插件设置 -> **Custom Prompt Instructions**。 |
| **ChatGPT Canvas** | 个人设置 -> 个性化 -> **自定义指令 (Custom Instructions)**。 |
| **Google IDX** | 云端 IDE 设置 -> **AI Rules**。 |

---

## 🎯 注入后的验证

注入完成后，开启一个新对话并输入：
`你好` 或 `Hi`

**预期结果**：
AI 应该立即响应类似以下内容：
> “God Mode Active. Initializing project governance... 我已检测到 `AGENTS.md` 协议并完成初始化。我是您的 Agents-MD 治理助手，请问今天有什么可以帮您？”

---

> **注意**：如果工具同时支持全局规则和项目级规则（如 Cursor 支持 `.cursorrules`），建议在项目根目录也放置一份副本以确保双重保险。
