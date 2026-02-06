---
name: git-commit
description: 智能生成 Git 提交信息
---

# Smart Git Commit Skill

## 📋 概述

基于代码变更自动生成规范的 Git 提交信息，遵循约定式提交（Conventional Commits）：

- 📝 **自动分析**：识别变更类型和范围
- 🎯 **规范格式**：符合团队提交规范
- 🔍 **详细描述**：生成有意义的提交信息
- 🚀 **提升效率**：减少手动编写时间

## 🔧 前置条件 (Prerequisites)

| 工具 | 用途 | 检查命令 | 安装参考 |
|-----|------|---------|---------|
| Git | 版本控制 | `git --version` | [git-scm.com](https://git-scm.com/) |

> **可选工具**:
>
> - **commitizen**: 交互式提交 (`npm install -g commitizen`)
> - **commitlint**: 提交信息验证 (`npm install --save-dev @commitlint/cli`)

## 🚀 使用方法

### 方法 1: 使用 AI 助手调用

```
"生成 Git 提交信息"
"分析我的代码变更并创建提交"
"根据暂存区生成 commit message"
```

AI 会：

1. 运行 `git status` 和 `git diff --staged`
2. 分析变更内容
3. 生成符合规范的提交信息
4. 提供 `git commit -m ...` 命令

### 方法 2: 使用 Commitizen

```bash
# 安装
npm install -g commitizen
cz-cli init cz-conventional-changelog --save-dev --save-exact

# 使用
git add .
git cz    # 或 cz
```

### 方法 3: 手动编写（遵循规范）

```bash
git commit -m "feat(auth): add OAuth2 login support"
git commit -m "fix(api): resolve null pointer in user profile endpoint"
git commit -m "docs(readme): update installation instructions"
```

## 🎯 提交信息格式

遵循 **Conventional Commits** 规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type（类型）- 必需

| type | 说明 | 示例 |
|------|------|------|
| **feat** | 新功能 | `feat(auth): add Google SSO` |
| **fix** | Bug 修复 | `fix(api): handle timeout errors` |
| **docs** | 文档更新 | `docs(api): update endpoint descriptions` |
| **style** | 代码格式（不影响功能） | `style: format code with Black` |
| **refactor** | 重构（不是新功能也不是 bug 修复） | `refactor(db): simplify query logic` |
| **perf** | 性能优化 | `perf(api): cache frequently accessed data` |
| **test** | 测试相关 | `test(auth): add unit tests for login` |
| **build** | 构建系统或外部依赖 | `build: upgrade webpack to v5` |
| **ci** | CI 配置文件和脚本 | `ci: add GitHub Actions workflow` |
| **chore** | 其他不修改 src 或 test 的更改 | `chore: update .gitignore` |
| **revert** | 回退之前的提交 | `revert: revert commit abc1234` |

### Scope（范围）- 可选

指明变更的模块或组件：

- `auth` - 认证模块
- `api` - API 相关
- `ui` - 用户界面
- `db` - 数据库
- `config` - 配置文件
- `deps` - 依赖项

### Subject（主题）- 必需

- 简短描述（<50 字符）
- 使用祈使句（"add" 而非 "added"）
- 首字母小写
- 结尾不加句号

### Body（正文）- 可选

- 详细说明变更的动机
- 对比之前的行为
- 每行 <72 字符

### Footer（页脚）- 可选

- Breaking Changes: `BREAKING CHANGE: <描述>`
- 关闭 Issue: `Closes #123, #456`
- 引用资源: `Refs #789`

## 📊 示例

### 简单提交

```bash
git commit -m "feat: add dark mode toggle"
git commit -m "fix: resolve login redirect issue"
git commit -m "docs: update API documentation"
```

### 带 scope 的提交

```bash
git commit -m "feat(auth): implement two-factor authentication"
git commit -m "fix(ui): correct button alignment on mobile"
git commit -m "refactor(api): extract common validation logic"
```

### 完整格式提交

```bash
git commit -m "feat(payment): integrate Stripe payment gateway

- Add Stripe SDK dependency
- Implement payment processing workflow  
- Add webhook for payment status updates
- Include error handling for failed transactions

Closes #234"
```

### Breaking Change 提交

```bash
git commit -m "feat(api)!: change authentication endpoint structure

BREAKING CHANGE: The /auth/login endpoint now requires email instead of username.
Migration guide: Update all API clients to send 'email' field instead of 'username'.

Refs #456"
```

## ⚙️ 配置文件

### .commitlintrc.json (commitlint)

```json
{
  "extends": ["@commitlint/config-conventional"],
  "rules": {
    "type-enum": [
      2,
      "always",
      [
        "feat", "fix", "docs", "style", "refactor",
        "perf", "test", "build", "ci", "chore", "revert"
      ]
    ],
    "type-case": [2, "always", "lower-case"],
    "subject-case": [2, "never", ["upper-case"]],
    "subject-empty": [2, "never"],
    "subject-full-stop": [2, "never", "."],
    "header-max-length": [2, "always", 100]
  }
}
```

### .cz.json (Commitizen)

```json
{
  "path": "cz-conventional-changelog",
  "types": {
    "feat": {
      "description": "A new feature",
      "title": "Features"
    },
    "fix": {
      "description": "A bug fix",
      "title": "Bug Fixes"
    }
  },
  "scopes": ["auth", "api", "ui", "db", "config"]
}
```

### package.json (Husky + commitlint)

```json
{
  "husky": {
    "hooks": {
      "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    }
  }
}
```

## 🔄 CI/CD 集成

### Pre-commit Hook

```bash
# .git/hooks/commit-msg
#!/bin/sh
npx --no-install commitlint --edit $1
```

### GitHub Actions

```yaml
name: Lint Commits
on: [pull_request]

jobs:
  commitlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - uses: wagoid/commitlint-github-action@v5
```

## 🆘 常见问题

**Q: 如何修改上一次提交信息？**  
A: `git commit --amend -m "新的提交信息"`

**Q: 如何为多个变更生成提交信息？**  
A:

1. 分别暂存：`git add file1` → `git commit` → `git add file2` → `git commit`
2. 或使用交互式：`git add -p`

**Q: 什么时候需要 Breaking Change？**  
A: 当变更导致现有功能不兼容时（API 变更、配置格式改变等）

**Q: Scope 是必须的吗？**  
A: 不是必须，但强烈推荐，有助于快速理解变更范围

**Q: 如何强制团队遵循规范？**  
A:

1. 添加 commitlint + Husky pre-commit hook
2. CI 中验证提交信息格式
3. PR 模板中说明规范

## 🔗 相关资源

- [Conventional Commits 规范](https://www.conventionalcommits.org/)
- [Commitizen](https://github.com/commitizen/cz-cli)
- [commitlint](https://commitlint.js.org/)
- [如何编写 Git 提交信息](https://chris.beams.io/posts/git-commit/)
- [Semantic Versioning](https://semver.org/)
