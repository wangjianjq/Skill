---
name: lint-python
description: Check Python code quality with Ruff
---

# Python Lint Skill

## 📋 Overview

Use **Ruff** to check Python code quality, an extremely fast Python linter written in Rust:

- 🚀 **10-100x faster than traditional linters** (Flake8, Pylint)
- 🔄 **Replaces multiple tools**: Flake8, isort, pyupgrade, autoflake
- 📏 **800+ rules**: Covering code style, error detection, performance optimization
- 🔧 **Auto-fix**: One-click fix for most issues

## 🔧 Prerequisites

| Tool | Min Version | Check Command | Installation |
|------|-------------|---------------|--------------|
| Python | 3.8+ | `python --version` | [python.org](https://python.org) |
| Ruff | 0.1.0+ | `ruff --version` | `pip install ruff` or `pipx install ruff` |

> **Note**: The script will auto-detect if Ruff is installed and provide a friendly prompt if missing.

## 🚀 Usage

### Method 1: Use AI Assistant

```
"Use lint-python skill to check my code"
"Check Python code quality with Ruff"
```

### Method 2: Run Script Directly

**Windows (PowerShell):**

```powershell
.\.agent\skills\lint-python\scripts\lint.ps1
```

**Linux/Mac (Bash):**

```bash
./.agent/skills/lint-python/scripts/lint.sh
```

### Method 3: With Parameters

**Check specific directory:**

```powershell
# Windows
.\.agent\skills\lint-python\scripts\lint.ps1 -Path ".\src"

# Linux/Mac  
./.agent/skills/lint-python/scripts/lint.sh src
```

**Auto-fix issues:**

```powershell
# Windows
.\.agent\skills\lint-python\scripts\lint.ps1 -Fix

# Linux/Mac
./.agent/skills/lint-python/scripts/lint.sh --fix
```

**Show errors only (ignore warnings):**

```powershell
# Windows
.\.agent\skills\lint-python\scripts\lint.ps1 -ErrorsOnly

# Linux/Mac
./.agent/skills/lint-python/scripts/lint.sh --errors-only
```

## 🎯 What It Checks

### Code Style (Pycodestyle)

- ✅ PEP 8 compliance
- ✅ Indentation and whitespace
- ✅ Line length limits
- ✅ Naming conventions

### Error Detection (Pyflakes)

- ✅ Unused imports and variables
- ✅ Undefined names
- ✅ Duplicate keys
- ✅ Invalid print statements

### Import Sorting (isort)

- ✅ Import statement grouping
- ✅ Alphabetical ordering
- ✅ Stdlib/third-party/local separation

### Code Upgrade (pyupgrade)

- ✅ Old syntax detection (e.g., `%` formatting)
- ✅ Type annotation simplification
- ✅ Recommend modern Python patterns

### Performance and Best Practices

- ✅ List comprehension optimization
- ✅ f-string recommendation
- ✅ Set operation efficiency
- ✅ Exception handling standards

## 📊 Output Example

```
🐍 Python Lint - Checking code...

✅ Python: Python 3.11.7
✅ Ruff: ruff 0.2.1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📁 Scanning directory: C:\Users\WJ\Project\src
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

src/main.py:15:1: F401 [*] `os` imported but unused
    |
 15 | import os
    | ^^^^^^^^^ F401
    |
    = help: Remove unused import: `os`

src/utils.py:42:5: E501 Line too long (95 > 88 characters)
    |
 42 |     return f"Processing data from {source} with parameters {params_dict}"
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ E501

src/config.py:23:5: S105 Possible hardcoded password: "secret123"
    |
 23 |     password = "secret123"
    |     ^^^^^^^^^^^^^^^^^^^^^^ S105

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Check Results:
   ✅ Passed: 12 files
   ⚠️  Warnings: 1 issue (E501)
   ❌ Errors: 2 issues (F401, S105)

💡 Tips:
   - Run lint.ps1 -Fix to auto-fix F401
   - Security issue S105 requires manual handling
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## ⚙️ Configuration

Create `pyproject.toml` or `ruff.toml` in the project root:

### pyproject.toml

```toml
[tool.ruff]
# Set line length
line-length = 88

# Target Python version
target-version = "py38"

# Excluded directories
exclude = [
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
]

[tool.ruff.lint]
# Enabled rule sets
select = [
    "E",     # pycodestyle errors
    "W",     # pycodestyle warnings
    "F",     # pyflakes
    "I",     # isort
    "N",     # pep8-naming
    "S",     # flake8-bandit (security)
    "B",     # flake8-bugbear
    "C90",   # mccabe complexity
    "UP",    # pyupgrade
]

# Ignored rules
ignore = [
    "E501",  # Line length (handled by formatter)
]

# Per-file ignores
[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]  # Allow unused imports
"tests/*" = ["S101"]      # Allow assert statements

[tool.ruff.lint.mccabe]
# Maximum complexity
max-complexity = 10
```

### ruff.toml (Simplified)

```toml
line-length = 88
target-version = "py38"

[lint]
select = ["E", "F", "I", "N", "S", "B"]
ignore = ["E501"]

[lint.per-file-ignores]
"__init__.py" = ["F401"]
```

## 🔄 CI/CD Integration

### GitHub Actions

```yaml
name: Python Lint
on: [push, pull_request]

jobs:
  ruff:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install Ruff
        run: pip install ruff
      
      - name: Run Ruff
        run: ruff check .
```

### GitLab CI

```yaml
ruff:
  image: python:3.11
  script:
    - pip install ruff
    - ruff check .
  only:
    - merge_requests
    - main
```

### Pre-commit Hook

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.1
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
```

## 🆘 FAQ

**Q: What's the difference between Ruff and Flake8/Pylint?**  
A: Ruff is 10-100x faster and consolidates multiple tools, reducing configuration complexity

**Q: What if Ruff is not installed?**  
A: The script will auto-detect and prompt installation:

```bash
pip install ruff        # Local install
pipx install ruff       # Global install (recommended)
```

**Q: How to ignore warnings on specific lines?**  
A: Use inline comments:

```python
import os  # noqa: F401
password = "temp"  # noqa: S105
```

**Q: How to see all available rules?**  
A: Run `ruff linter` or visit [Ruff Rules](https://docs.astral.sh/ruff/rules/)

**Q: Can all issues be auto-fixed?**  
A: Some issues can be auto-fixed with `--fix`. Security issues require manual review

**Q: Is it compatible with Black formatter?**  
A: Fully compatible! Ruff's formatting is 100% compatible with Black

## 🔗 Related Resources

- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Ruff Rules List](https://docs.astral.sh/ruff/rules/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Ruff GitHub](https://github.com/astral-sh/ruff)
