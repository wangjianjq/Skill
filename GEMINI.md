# Gemini CLI Context & Protocol

> **Protocol**: Agents-MD Pro v7.5 | **Philosophy**: Zero-Decision Burden

## 🚨 PRIME DIRECTIVE

1. Read `AGENTS.md` in root directory for full protocol
2. Execute `[BOOT_SEQUENCE]` before ANY development request
3. Do NOT read `README.txt` (Human only)

## 📜 Core Rules (Embedded)

### Territory Control

- 🔴 `.agents/*` = **READ-ONLY** (except `sandbox/`)
- 🟢 All other paths = **READ-WRITE**

### Language Mirroring (语言镜像)

**MANDATORY RULE** - Match user's dialogue language in **ALL** artifacts:

- Chinese user -> `task.md`, `implementation_plan.md`, `walkthrough.md`, ALL tool call descriptions in **Chinese**
- English user -> ALL artifacts in **English**
- **Detection**: Check last 3 user messages; if ≥2 in Language X, use Language X
- **Self-Check**: Before creating ANY artifact, verify language matches user's dialogue
- **Violation**: Artifacts in wrong language are INVALID and must be rewritten immediately

### Safety Override

- Destructive commands require pass-phrase: `I-CONFIRM` or `我已明确确认`
- Double confirmation mandatory

### Development Flow

1. Scope Confirmation → 2. Mini Design (3-7 lines) → 3. Implementation → 4. Self-Testing → 5. CHANGELOG Update

## 🧠 Gemini CLI-Specific Features

- Use `/tools` to list available MCP tools
- Use `@file` to reference specific files
- Use sandbox mode for safe code execution
- Leverage multimodal capabilities for image analysis

## 📂 Quick Reference

| Resource | Path |
| :--- | :--- |
| Full Protocol | `AGENTS.md` |
| Governance | `PROJECT_GOVERNANCE.md` |
| Status | `PROJECT_STATUS.md` |
| Knowledge Index | `AGENTS_INDEX.yaml` |
| Memory | `context/memory.md` |
| Project State | `context/status.md` (auto-generated) |

## 🔄 Context System

- **Status File**: `context/status.md` - Auto-generated project status
- **Status Generator**: `context/auto_status.py` - Run manually or via Git hooks
- **Prompt Builder**: `make_prompt.py` - Assembles context for AI (tiered strategy for large projects)
