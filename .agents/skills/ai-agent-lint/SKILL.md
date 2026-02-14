---
name: ai-agent-lint
description: AI Agent code quality check - Use Ruff to check code standards for LangChain, AutoGen, and other AI Agent projects
---

# AI Agent Lint Skill

## 📋 Overview

This skill uses **Ruff** (an extremely fast Python linter) to check AI Agent project code quality, specifically targeting:

- LangChain applications
- AutoGen multi-agent systems
- CrewAI collaborative agents
- General AI Agent development projects

## 🔧 Prerequisites

| Tool | Min Version | Check Command | Installation |
|------|-------------|---------------|--------------|
| Python | 3.10+ | `python --version` | [python.org](https://python.org) |
| Ruff | 0.1.0+ | `ruff --version` | `pip install ruff` |

> **Note**: If Ruff is not installed, the script will provide a friendly prompt instead of failing.

## 🚀 Usage

### Method 1: Use AI Assistant

Tell the AI directly:

```
"Use ai-agent-lint skill to check my project"
```

AI will automatically:

1. Read this SKILL.md to understand usage
2. Execute the check script
3. Report found issues

### Method 2: Run Script Directly

**Windows (PowerShell):**

```powershell
.\.agents\skills\ai-agent-lint\scripts\lint.ps1
```

**Linux/Mac (Bash):**

```bash
./.agents/skills/ai-agent-lint/scripts/lint.sh
```

### Method 3: Specify Target Directory

```powershell
# Windows
.\.agents\skills\ai-agent-lint\scripts\lint.ps1 -Path ".\src"

# Linux/Mac
./.agents/skills/ai-agent-lint/scripts/lint.sh src
```

## 🎯 What It Checks

### Python Code Standards

- ✅ PEP 8 style compliance
- ✅ Type hint completeness
- ✅ Import statement ordering
- ✅ Unused variables and imports
- ✅ Code complexity check

### AI Agent Specific Checks

- ✅ Prompt template string safety
- ✅ Hardcoded API key detection
- ✅ Async code patterns
- ✅ Error handling completeness
- ✅ Resource leak detection (unclosed LLM clients)

### Security Checks

- ⚠️ `eval()` and `exec()` usage warnings
- ⚠️ SQL injection risks
- ⚠️ Sensitive data logging
- ⚠️ Unsafe deserialization

## 📊 Output Example

```
🔍 AI Agent Lint - Checking project...

📁 Scanning directory: C:\Users\WJ\Desktop\MyAgent
📦 Detected: LangChain project

✅ src/main.py - No issues
⚠️  src/agent.py:15:1 - F401 [unused-import] 'os' imported but unused
❌ src/config.py:23:5 - S105 [hardcoded-password-string] Possible hardcoded password

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Check Results:
   ✅ Passed: 45 files
   ⚠️  Warnings: 3 issues
   ❌ Errors: 1 issue
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Tip: Run 'ruff check --fix' to auto-fix some issues
```

## ⚙️ Configuration

Create `pyproject.toml` or `ruff.toml` in the project root to customize rules:

```toml
# pyproject.toml
[tool.ruff]
line-length = 88
target-version = "py310"

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # pyflakes
    "I",    # isort
    "N",    # pep8-naming
    "S",    # flake8-bandit (security)
    "B",    # flake8-bugbear
    "C90",  # mccabe complexity
]
ignore = ["E501"]  # Ignore line length limit

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py
```

## 🔗 Related Resources

- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [LangChain Development Guide](https://python.langchain.com/docs/get_started/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)

## 🆘 FAQ

**Q: What if Ruff is not installed?**  
A: The script will detect and prompt installation: `pip install ruff`

**Q: Can it be integrated into CI/CD?**  
A: Yes! Add to GitHub Actions:

```yaml
- name: Lint AI Agent Code
  run: |
    pip install ruff
    ruff check .
```

**Q: How to auto-fix issues?**  
A: Run `ruff check --fix` or use the script's `--fix` parameter

**Q: Does it support other AI frameworks?**  
A: Yes, it supports all Python-based AI Agent frameworks with universal rules

