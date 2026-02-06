---
name: lint-js
description: 使用 ESLint 检查 JavaScript/TypeScript 代码质量
---

# JavaScript/TypeScript Lint Skill

## 📋 概述

使用 **ESLint** 检查 JavaScript 和 TypeScript 代码质量：

- 🔍 **错误检测**：发现潜在bug和问题
- 📏 **风格检查**：统一代码风格
- 🔧 **自动修复**：一键修复常见问题
- 🎯 **可配置**：支持多种规则集

## 🔧 前置条件 (Prerequisites)

| 工具 | 最低版本 | 检查命令 | 安装参考 |
|-----|---------|---------|---------|
| Node.js | 16+ | `node --version` | [nodejs.org](https://nodejs.org) |
| ESLint | 8.0+ | `eslint --version` | `npm install -g eslint` |

## 🚀 使用方法

### 方法 1: AI 助手调用

```
"使用 lint-js 检查我的 JavaScript 代码"
```

### 方法 2: 直接运行脚本

```powershell
# Windows
.\.agent\skills\lint-js\scripts\lint.ps1

# Linux/Mac
./.agent/skills/lint-js/scripts/lint.sh
```

### 方法 3: 指定参数

```powershell
# 自动修复
.\.agent\skills\lint-js\scripts\lint.ps1 -Fix

# 指定文件类型
.\.agent\skills\lint-js\scripts\lint.ps1 -Extensions "ts,tsx"
```

## 🎯 检查内容

### 代码质量

- ✅ 未使用的变量
- ✅ 未定义的变量
- ✅ 重复代码检测
- ✅ 复杂度检查

### 最佳实践

- ✅ 严格模式
- ✅ 箭头函数使用
- ✅ Promise 处理
- ✅ async/await 规范

### TypeScript 特定

- ✅ 类型安全检查
- ✅ 接口规范
- ✅ 命名约定
- ✅ 导入排序

## ⚙️ 配置文件

```json
// .eslintrc.json
{
  "env": {
    "browser": true,
    "es2021": true,
    "node": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module"
  },
  "rules": {
    "no-unused-vars": "warn",
    "no-console": "off",
    "quotes": ["error", "single"],
    "semi": ["error", "always"]
  }
}
```

## 🔗 相关资源

- [ESLint 文档](https://eslint.org/)
- [TypeScript ESLint](https://typescript-eslint.io/)
