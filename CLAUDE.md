# Claude Code Context & Protocol

> **Protocol**: Agents-MD Pro v8.0 | **Philosophy**: Zero-Decision Burden

## 🚨 PRIME DIRECTIVE

1. Read `AGENTS.md` in root directory for full protocol
2. Execute `[BOOT_SEQUENCE]` before ANY development request
3. Do NOT read `README.md` (Human only)

## 📜 Core Rules (Embedded)

### Territory Control

- 🔴 `.agents/*` = **READ-ONLY** (except `sandbox/`)
- 🟢 All other paths = **READ-WRITE**

### Language Mirroring

- Match user's dialogue language in all artifacts
- Chinese user → Chinese artifacts; English user → English artifacts

### Safety Override

- Destructive commands require pass-phrase: `I-CONFIRM` or `我已明确确认`
- Double confirmation mandatory

### Development Flow

1. Scope Confirmation → 2. Mini Design (3-7 lines) → 3. Implementation → 4. Self-Testing → 5. CHANGELOG Update

## 🤖 Claude Code-Specific Features

- Use `/add` to include files in context
- Use `/compact` to reduce context when running low
- Use `/cost` to check token usage
- Use `/clear` to start fresh context

## 📂 Quick Reference

| Resource | Path |
| :--- | :--- |
| Full Protocol | `AGENTS.md` |
| Governance | `PROJECT_GOVERNANCE.md` |
| Status | `PROJECT_STATUS.md` |
| Knowledge Index | `AGENTS_INDEX.yaml` |
| Memory | `context/memory.md` |

