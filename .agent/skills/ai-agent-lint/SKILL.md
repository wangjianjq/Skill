---
name: ai-agent-lint
description: AI Agent 代码质量检查 - 使用 Ruff 检查 LangChain、AutoGen 等 AI Agent 项目的代码规范
---

# AI Agent Lint Skill

## 📋 概述

此 skill 使用 **Ruff**（超快的 Python linter）检查 AI Agent 项目代码质量，专门针对：

- LangChain 应用
- AutoGen 多代理系统
- CrewAI 协作代理
- 通用 AI Agent 开发项目

## 🔧 前置条件 (Prerequisites)

| 工具 | 最低版本 | 检查命令 | 安装参考 |
|-----|---------|---------|---------|
| Python | 3.10+ | `python --version` | [python.org](https://python.org) |
| Ruff | 0.1.0+ | `ruff --version` | `pip install ruff` |

> **注意**：如果未安装 Ruff，脚本会给出友好提示，而不会失败。

## 🚀 使用方法

### 方法 1: 使用 AI 助手调用

直接告诉 AI：

```
"使用 ai-agent-lint skill 检查我的项目"
```

AI 会自动：

1. 读取此 SKILL.md 了解用法
2. 执行检查脚本
3. 报告发现的问题

### 方法 2: 直接运行脚本

**Windows (PowerShell):**

```powershell
.\.agent\skills\ai-agent-lint\scripts\lint.ps1
```

**Linux/Mac (Bash):**

```bash
./.agent/skills/ai-agent-lint/scripts/lint.sh
```

### 方法 3: 指定目标目录

```powershell
# Windows
.\.agent\skills\ai-agent-lint\scripts\lint.ps1 -Path ".\src"

# Linux/Mac
./.agent/skills/ai-agent-lint/scripts/lint.sh src
```

## 🎯 检查内容

### Python 代码规范

- ✅ PEP 8 风格规范
- ✅ 类型提示完整性
- ✅ Import 语句排序
- ✅ 未使用的变量和导入
- ✅ 代码复杂度检查

### AI Agent 特定检查

- ✅ Prompt 模板字符串安全性
- ✅ API 密钥硬编码检测
- ✅ 异步代码模式
- ✅ 错误处理完整性
- ✅ 资源泄漏检测（LLM 客户端未关闭）

### 安全性检查

- ⚠️ `eval()` 和 `exec()` 使用警告
- ⚠️ SQL 注入风险
- ⚠️ 敏感数据记录
- ⚠️ 不安全的反序列化

## 📊 输出示例

```
🔍 AI Agent Lint - 正在检查项目...

📁 扫描目录: C:\Users\WJ\Desktop\MyAgent
📦 检测到: LangChain 项目

✅ src/main.py - 无问题
⚠️  src/agent.py:15:1 - F401 [unused-import] 'os' imported but unused
❌ src/config.py:23:5 - S105 [hardcoded-password-string] Possible hardcoded password

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 检查结果:
   ✅ 通过: 45 个文件
   ⚠️  警告: 3 个问题
   ❌ 错误: 1 个问题
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 提示: 运行 'ruff check --fix' 可自动修复部分问题
```

## ⚙️ 配置文件

在项目根目录创建 `pyproject.toml` 或 `ruff.toml` 自定义规则：

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
ignore = ["E501"]  # 忽略行长度限制

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]  # 允许 __init__.py 中未使用的导入
```

## 🔗 相关资源

- [Ruff 官方文档](https://docs.astral.sh/ruff/)
- [LangChain 开发指南](https://python.langchain.com/docs/get_started/)
- [PEP 8 风格指南](https://peps.python.org/pep-0008/)

## 🆘 常见问题

**Q: Ruff 未安装怎么办？**  
A: 脚本会检测并提示安装命令：`pip install ruff`

**Q: 可以集成到 CI/CD 吗？**  
A: 可以！在 GitHub Actions 中添加：

```yaml
- name: Lint AI Agent Code
  run: |
    pip install ruff
    ruff check .
```

**Q: 如何自动修复问题？**  
A: 运行 `ruff check --fix` 或使用脚本的 `--fix` 参数

**Q: 支持其他 AI 框架吗？**  
A: 支持所有基于 Python 的 AI Agent 框架，规则通用
