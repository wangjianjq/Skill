---
name: lint-python
description: 使用 Ruff 检查 Python 代码质量
---

# Python Lint Skill

## 📋 概述

使用 **Ruff** 检查 Python 代码质量，这是一个极速的 Python linter，用 Rust 编写：

- 🚀 **10-100x 快于传统 linter**（Flake8、Pylint）
- 🔄 **替代多个工具**：Flake8, isort, pyupgrade, autoflake
- 📏 **800+ 规则**：涵盖代码风格、错误检测、性能优化
- 🔧 **自动修复**：一键修复大部分问题

## 🔧 前置条件 (Prerequisites)

| 工具 | 最低版本 | 检查命令 | 安装参考 |
|-----|---------|---------|---------|
| Python | 3.8+ | `python --version` | [python.org](https://python.org) |
| Ruff | 0.1.0+ | `ruff --version` | `pip install ruff` 或 `pipx install ruff` |

> **注意**：脚本会自动检测 Ruff 是否安装，缺失时给出友好提示。

## 🚀 使用方法

### 方法 1: 使用 AI 助手调用

```
"使用 lint-python skill 检查我的代码"
"用 Ruff 检查 Python 代码质量"
```

### 方法 2: 直接运行脚本

**Windows (PowerShell):**

```powershell
.\.agent\skills\lint-python\scripts\lint.ps1
```

**Linux/Mac (Bash):**

```bash
./.agent/skills/lint-python/scripts/lint.sh
```

### 方法 3: 指定参数

**检查特定目录:**

```powershell
# Windows
.\.agent\skills\lint-python\scripts\lint.ps1 -Path ".\src"

# Linux/Mac  
./.agent/skills/lint-python/scripts/lint.sh src
```

**自动修复问题:**

```powershell
# Windows
.\.agent\skills\lint-python\scripts\lint.ps1 -Fix

# Linux/Mac
./.agent/skills/lint-python/scripts/lint.sh --fix
```

**仅显示错误（忽略警告）:**

```powershell
# Windows
.\.agent\skills\lint-python\scripts\lint.ps1 -ErrorsOnly

# Linux/Mac
./.agent/skills/lint-python/scripts/lint.sh --errors-only
```

## 🎯 检查内容

### 代码风格 (Pycodestyle)

- ✅ PEP 8 规范遵循
- ✅ 缩进和空白
- ✅ 行长度限制
- ✅ 命名约定

### 错误检测 (Pyflakes)

- ✅ 未使用的导入和变量
- ✅ 未定义的名称
- ✅ 重复的键
- ✅ 无效的打印语句

### Import 排序 (isort)

- ✅ Import 语句分组
- ✅ 字母顺序排序
- ✅ 标准库/第三方/本地分离

### 代码升级 (pyupgrade)

- ✅ 旧式语法检测（如 `%` 格式化）
- ✅ 类型注解简化
- ✅ 推荐现代 Python 写法

### 性能和最佳实践

- ✅ 列表推导优化
- ✅ f-string 推荐
- ✅ 集合操作效率
- ✅ 异常处理规范

## 📊 输出示例

```
🐍 Python Lint - 正在检查代码...

✅ Python: Python 3.11.7
✅ Ruff: ruff 0.2.1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📁 扫描目录: C:\Users\WJ\Project\src
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
📊 检查结果:
   ✅ 通过: 12 个文件
   ⚠️  警告: 1 个问题（E501）
   ❌ 错误: 2 个问题（F401, S105）

💡 提示:
   - 运行 lint.ps1 -Fix 可自动修复 F401
   - 安全问题 S105 需要手动处理
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## ⚙️ 配置文件

在项目根目录创建 `pyproject.toml` 或 `ruff.toml`：

### pyproject.toml

```toml
[tool.ruff]
# 设置行长度
line-length = 88

# 目标 Python 版本
target-version = "py38"

# 排除目录
exclude = [
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
]

[tool.ruff.lint]
# 启用的规则集
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

# 忽略特定规则
ignore = [
    "E501",  # 行长度（由 formatter 处理）
]

# 每个文件的忽略规则
[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]  # 允许未使用的导入
"tests/*" = ["S101"]      # 允许 assert 语句

[tool.ruff.lint.mccabe]
# 最大复杂度
max-complexity = 10
```

### ruff.toml (简化版)

```toml
line-length = 88
target-version = "py38"

[lint]
select = ["E", "F", "I", "N", "S", "B"]
ignore = ["E501"]

[lint.per-file-ignores]
"__init__.py" = ["F401"]
```

## 🔄 CI/CD 集成

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

## 🆘 常见问题

**Q: Ruff 和 Flake8/Pylint 有什么区别？**  
A: Ruff 性能快 10-100 倍，并整合了多个工具的功能，减少配置复杂度

**Q: Ruff 未安装怎么办？**  
A: 脚本会自动检测并提示安装：

```bash
pip install ruff        # 本地安装
pipx install ruff       # 全局安装（推荐）
```

**Q: 如何忽略特定行的警告？**  
A: 使用行内注释：

```python
import os  # noqa: F401
password = "temp"  # noqa: S105
```

**Q: 如何查看所有可用规则？**  
A: 运行 `ruff linter` 或访问 [Ruff Rules](https://docs.astral.sh/ruff/rules/)

**Q: 可以自动修复所有问题吗？**  
A: 部分问题可以自动修复，使用 `--fix` 参数。安全性问题需手动审查

**Q: 与 Black 格式化工具兼容吗？**  
A: 完全兼容！Ruff 的格式化与 Black 100% 兼容

## 🔗 相关资源

- [Ruff 官方文档](https://docs.astral.sh/ruff/)
- [Ruff 规则列表](https://docs.astral.sh/ruff/rules/)
- [PEP 8 风格指南](https://peps.python.org/pep-0008/)
- [Ruff GitHub](https://github.com/astral-sh/ruff)
