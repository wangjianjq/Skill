---
name: git-commit
description: Smart Git commit message generation
---

# Smart Git Commit Skill

## 📋 Overview

Automatically generate standardized Git commit messages based on code changes, following Conventional Commits:

- 📝 **Auto-analysis**: Identify change type and scope
- 🎯 **Standard format**: Comply with team commit standards
- 🔍 **Detailed description**: Generate meaningful commit messages
- 🚀 **Boost efficiency**: Reduce manual writing time

## 🔧 Prerequisites

| Tool | Purpose | Check Command | Installation |
|------|---------|---------------|--------------|
| Git | Version control | `git --version` | [git-scm.com](https://git-scm.com/) |

> **Optional tools**:
>
> - **commitizen**: Interactive commits (`npm install -g commitizen`)
> - **commitlint**: Commit message validation (`npm install --save-dev @commitlint/cli`)

## 🚀 Usage

### Method 1: Use AI Assistant

```
"Generate Git commit message"
"Analyze my code changes and create a commit"
"Generate commit message based on staged changes"
```

AI will:

1. Run `git status` and `git diff --staged`
2. Analyze change content
3. Generate standard-compliant commit message
4. Provide `git commit -m ...` command

### Method 2: Use Commitizen

```bash
# Install
npm install -g commitizen
cz-cli init cz-conventional-changelog --save-dev --save-exact

# Usage
git add .
git cz    # or cz
```

### Method 3: Write Manually (Following Standard)

```bash
git commit -m "feat(auth): add OAuth2 login support"
git commit -m "fix(api): resolve null pointer in user profile endpoint"
git commit -m "docs(readme): update installation instructions"
```

## 🎯 Commit Message Format

Following **Conventional Commits** standard:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type - Required

| type | Description | Example |
|------|-------------|---------|
| **feat** | New feature | `feat(auth): add Google SSO` |
| **fix** | Bug fix | `fix(api): handle timeout errors` |
| **docs** | Documentation update | `docs(api): update endpoint descriptions` |
| **style** | Code formatting (no logic change) | `style: format code with Black` |
| **refactor** | Refactoring (not feat or fix) | `refactor(db): simplify query logic` |
| **perf** | Performance optimization | `perf(api): cache frequently accessed data` |
| **test** | Test related | `test(auth): add unit tests for login` |
| **build** | Build system or dependencies | `build: upgrade webpack to v5` |
| **ci** | CI config files and scripts | `ci: add GitHub Actions workflow` |
| **chore** | Other changes not modifying src/test | `chore: update .gitignore` |
| **revert** | Revert previous commit | `revert: revert commit abc1234` |

### Scope - Optional

Specify the module or component being changed:

- `auth` - Authentication module
- `api` - API related
- `ui` - User interface
- `db` - Database
- `config` - Configuration
- `deps` - Dependencies

### Subject - Required

- Short description (<50 characters)
- Use imperative mood ("add" not "added")
- Lowercase first letter
- No period at end

### Body - Optional

- Explain motivation for change
- Compare to previous behavior
- Each line <72 characters

### Footer - Optional

- Breaking Changes: `BREAKING CHANGE: <description>`
- Close Issue: `Closes #123, #456`
- Reference: `Refs #789`

## 📊 Examples

### Simple Commit

```bash
git commit -m "feat: add dark mode toggle"
git commit -m "fix: resolve login redirect issue"
git commit -m "docs: update API documentation"
```

### With Scope

```bash
git commit -m "feat(auth): implement two-factor authentication"
git commit -m "fix(ui): correct button alignment on mobile"
git commit -m "refactor(api): extract common validation logic"
```

### Full Format

```bash
git commit -m "feat(payment): integrate Stripe payment gateway

- Add Stripe SDK dependency
- Implement payment processing workflow  
- Add webhook for payment status updates
- Include error handling for failed transactions

Closes #234"
```

### Breaking Change

```bash
git commit -m "feat(api)!: change authentication endpoint structure

BREAKING CHANGE: The /auth/login endpoint now requires email instead of username.
Migration guide: Update all API clients to send 'email' field instead of 'username'.

Refs #456"
```

## ⚙️ Configuration

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

## 🔄 CI/CD Integration

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

## 🆘 FAQ

**Q: How to modify the last commit message?**  
A: `git commit --amend -m "new commit message"`

**Q: How to generate commit messages for multiple changes?**  
A:

1. Stage separately: `git add file1` → `git commit` → `git add file2` → `git commit`
2. Or use interactive: `git add -p`

**Q: When is Breaking Change needed?**  
A: When changes cause existing functionality to be incompatible (API changes, config format changes, etc.)

**Q: Is Scope required?**  
A: Not required, but strongly recommended for quick understanding of change scope

**Q: How to enforce team compliance?**  
A:

1. Add commitlint + Husky pre-commit hook
2. Validate commit message format in CI
3. Include standards in PR template

## 🔗 Related Resources

- [Conventional Commits Specification](https://www.conventionalcommits.org/)
- [Commitizen](https://github.com/commitizen/cz-cli)
- [commitlint](https://commitlint.js.org/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- [Semantic Versioning](https://semver.org/)
