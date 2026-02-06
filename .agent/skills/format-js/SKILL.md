---
name: format-js
description: 使用 Prettier 格式化 JavaScript/TypeScript 代码
---

# JavaScript/TypeScript Format Skill

## 📋 概述

使用 **Prettier** 自动格式化 JavaScript 和 TypeScript 代码：

- 🎨 **一致风格**：多种文件类型统一格式化
- ⚡ **快速执行**：毫秒级格式化速度
- 🔧 **开箱即用**：合理的默认配置
- 🌈 **广泛支持**：JS、TS、JSX、TSX、JSON、CSS 等

## 🔧 前置条件 (Prerequisites)

| 工具 | 最低版本 | 检查命令 | 安装参考 |
|-----|---------|---------|---------|
| Node.js | 16+ | `node --version` | [nodejs.org](https://nodejs.org) |
| Prettier | 2.8+ | `prettier --version` | `npm install -g prettier` |

## 🚀 使用方法

### 方法 1: AI 助手调用

```
"使用 format-js 格式化我的 JavaScript 代码"
```

### 方法 2: 直接运行脚本

```powershell
# Windows
.\.agent\skills\format-js\scripts\format.ps1

# Linux/Mac
./.agent/skills/format-js/scripts/format.sh
```

### 方法 3: 指定参数

```powershell
# 检查但不修改
.\.agent\skills\format-js\scripts\format.ps1 -Check

# 格式化特定文件类型
.\.agent\skills\format-js\scripts\format.ps1 -Extensions "js,ts,jsx,tsx"
```

## 🎯 格式化内容

- ✅ 缩进和空格
- ✅ 引号统一（单引号/双引号）
- ✅ 行长度限制
- ✅ 分号添加/删除
- ✅ 括号和逗号规范化
- ✅ 箭头函数格式

## ⚙️ 配置文件

```json
// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 80,
  "arrowParens": "avoid"
}
```

## 🔗 相关资源

- [Prettier 文档](https://prettier.io/)
- [Prettier Playground](https://prettier.io/playground/)
