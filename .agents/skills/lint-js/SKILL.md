---
name: lint-js
description: Check JavaScript/TypeScript code quality with ESLint
---

# JavaScript/TypeScript Lint Skill

## 📋 Overview

Use **ESLint** to check JavaScript and TypeScript code quality:

- 🔍 **Error detection**: Find potential bugs and issues
- 📏 **Style check**: Unified code style
- 🔧 **Auto-fix**: One-click fix for common issues
- 🎯 **Configurable**: Supports multiple rule sets

## 🔧 Prerequisites

| Tool | Min Version | Check Command | Installation |
|------|-------------|---------------|--------------|
| Node.js | 16+ | `node --version` | [nodejs.org](https://nodejs.org) |
| ESLint | 8.0+ | `eslint --version` | `npm install -g eslint` |

## 🚀 Usage

### Method 1: AI Assistant

```
"Use lint-js to check my JavaScript code"
```

### Method 2: Run Script Directly

```powershell
# Windows
.\.agents\skills\lint-js\scripts\lint.ps1

# Linux/Mac
./.agents/skills/lint-js/scripts/lint.sh
```

### Method 3: With Parameters

```powershell
# Auto-fix
.\.agents\skills\lint-js\scripts\lint.ps1 -Fix

# Specific file types
.\.agents\skills\lint-js\scripts\lint.ps1 -Extensions "ts,tsx"
```

## 🎯 What It Checks

### Code Quality

- ✅ Unused variables
- ✅ Undefined variables
- ✅ Duplicate code detection
- ✅ Complexity check

### Best Practices

- ✅ Strict mode
- ✅ Arrow function usage
- ✅ Promise handling
- ✅ async/await standards

### TypeScript Specific

- ✅ Type safety check
- ✅ Interface standards
- ✅ Naming conventions
- ✅ Import sorting

## ⚙️ Configuration

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

## 🔗 Related Resources

- [ESLint Documentation](https://eslint.org/)
- [TypeScript ESLint](https://typescript-eslint.io/)

