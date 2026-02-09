# Claude Code & Projects Configuration

This file serves as the source of truth for Claude Code CLI and Claude Projects.

## 🏗️ Build & Test

- **Build**: `npm install` (JS) or `pip install -r requirements.txt` (Python)
- **Test**: `npm test` (JS) or `pytest` (Python)
- **Lint**: `npm run lint` (JS) or `ruff check .` (Python)

## 🛠️ Antigravity Skills (Commands)

This project uses specialized agents (Skills) for core tasks. Use these commands:

- **Format Code**: `node .agent/skills/format-js/script.js` (example) - *See SKILL.md for exact usage*
- **Lint Code**: *See .agent/skills/lint-js/SKILL.md*
- **Commit**: *See .agent/skills/git-commit/SKILL.md*

### Skills Index

- **format-js**: `.agent/skills/format-js/SKILL.md`
- **lint-js**: `.agent/skills/lint-js/SKILL.md`
- **format-python**: `.agent/skills/format-python/SKILL.md`
- **lint-python**: `.agent/skills/lint-python/SKILL.md`
- **generate-changelog**: `.agent/skills/generate-changelog/SKILL.md`
- **run-tests**: `.agent/skills/run-tests/SKILL.md`
- **security-check**: `.agent/skills/security-check/SKILL.md`

## 🧩 Style & Conventions

- Follow strict separation of concerns.
- Use the Skills for all formatting and linting to ensure consistency.
