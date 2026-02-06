---
name: format-python
description: 使用 Black 格式化 Python 代码
---

# Python Format Skill

## 📋 概述

使用 **Black** 自动格式化 Python 代码，这是一个不妥协的代码格式化工具：

- 🎨 **统一风格**：团队代码风格自动一致
- ⚡ **快速执行**：格式化速度极快
- 🔒 **确定性**：相同代码总是得到相同结果
- 🔧 **零配置**：开箱即用

## 🔧 前置条件 (Prerequisites)

| 工具 | 最低版本 | 检查命令 | 安装参考 |
|-----|---------|---------|---------|
| Python | 3.8+ | `python --version` | [python.org](https://python.org) |
| Black | 22.0+ | `black --version` | `pip install black` |

## 🚀 使用方法

### 方法 1: AI 助手调用

```
"使用 format-python 格式化我的代码"
```

### 方法 2: 直接运行脚本

```powershell
# Windows
.\.agent\skills\format-python\scripts\format.ps1

# Linux/Mac
./.agent/skills/format-python/scripts/format.sh
```

### 方法 3: 指定参数

```powershell
# 检查但不修改（预览模式）
.\.agent\skills\format-python\scripts\format.ps1 -Check

# 指定目录
.\.agent\skills\format-python\scripts\format.ps1 -Path ".\src"
```

## 🎯 格式化内容

- ✅ 缩进标准化（4 空格）
- ✅ 行长度限制（默认 88 字符）
- ✅ 字符串引号统一
- ✅ 括号和逗号规范化
- ✅ Import 语句格式化

## ⚙️ 配置文件

```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'
extend-exclude = '''
/(
  \.git
  | \.venv
  | build
  | dist
)/
'''
```

## 🔗 相关资源

- [Black 文档](https://black.readthedocs.io/)
