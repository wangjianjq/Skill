# Skills Index

This directory contains all available skills, each providing tools and best practices for a specific domain.

## 📚 Skill Categories

### 1. AI Agent Development

| Skill | Description | Core Tool | Status |
|-------|-------------|-----------|--------|
| [ai-agent-lint](./ai-agent-lint/SKILL.md) | AI Agent code quality check | Ruff | 🆕 Complete |

### 2. Cloud-Native & DevOps

| Skill | Description | Core Tool | Status |
|-------|-------------|-----------|--------|
| [docker-lint](./docker-lint/SKILL.md) | Dockerfile best practices check | hadolint | 🆕 Complete |
| [k8s-lint](./k8s-lint/SKILL.md) | Kubernetes YAML validation | kube-linter, kubeconform | 🆕 Docs |

### 3. SQL & Data Engineering

| Skill | Description | Core Tool | Status |
|-------|-------------|-----------|--------|
| [sql-lint](./sql-lint/SKILL.md) | SQL code style check | SQLFluff | 🆕 Docs |
| [db-migrate](./db-migrate/SKILL.md) | Database migration management | Flyway, Atlas | 🆕 Docs |

### 4. Rust & Python Development

| Skill | Description | Core Tool | Status |
|-------|-------------|-----------|--------|
| [rust-lint](./rust-lint/SKILL.md) | Rust code quality check | Clippy, Rustfmt | 🆕 Docs |
| [lint-python](./lint-python/SKILL.md) | Python code quality check | Ruff | ✨ Upgraded Complete |
| [format-python](./format-python/SKILL.md) | Python code formatting | Black | ✨ Upgraded Docs |

### 5. Security

| Skill | Description | Core Tool | Status |
|-------|-------------|-----------|--------|
| [owasp-scan](./owasp-scan/SKILL.md) | OWASP dependency vulnerability scan | OWASP Dependency-Check | 🆕 Docs |
| [vuln-scan](./vuln-scan/SKILL.md) | Multi-language dependency security scan | Safety CLI, OSV-Scanner | 🆕 Docs |
| [security-check](./security-check/SKILL.md) | Dependency security vulnerability check | npm audit, pip-audit, etc. | ✨ Upgraded Docs |

### 6. General Development Tools

| Skill | Description | Core Tool | Status |
|-------|-------------|-----------|--------|
| [lint-js](./lint-js/SKILL.md) | JavaScript/TypeScript code check | ESLint | ✨ Upgraded Complete |
| [format-js](./format-js/SKILL.md) | JavaScript/TypeScript code formatting | Prettier | ✨ Upgraded Docs |
| [run-tests](./run-tests/SKILL.md) | Run project test suite | Pytest, Jest, Mocha, etc. | ✨ Upgraded Docs |
| [git-commit](./git-commit/SKILL.md) | Smart Git commit message generation | Git, Commitizen | ✨ Upgraded Docs |
| [generate-changelog](./generate-changelog/SKILL.md) | Auto-generate project changelog | - | 📝 Basic |

---

**Legend**:

- 🆕 **Complete** = Newly created with full docs + cross-platform scripts
- 🆕 **Docs** = Newly created with full documentation only
- ✨ **Upgraded Complete** = Upgraded with full docs + cross-platform scripts
- ✨ **Upgraded Docs** = Upgraded with enhanced documentation
- 📝 **Basic** = Basic documentation with guidance only

## 📖 How to Use Skills

### Method 1: Let AI Call Automatically

Tell the AI directly:

```
"Use docker-lint skill to check my Dockerfile"
"Use sql-lint to validate schema.sql"
```

AI will automatically:

1. Read the corresponding SKILL.md to understand usage
2. Execute necessary scripts
3. Report check results

### Method 2: Run Scripts Directly

Each skill provides cross-platform scripts:

**Windows (PowerShell):**

```powershell
.\.agents\skills\<skill-name>\scripts\<script-name>.ps1
```

**Linux/Mac (Bash):**

```bash
./.agents/skills/<skill-name>/scripts/<script-name>.sh
```

### Method 3: Read Full Documentation

Read each skill's `SKILL.md` file to get:

- 📋 Prerequisites and dependencies
- 🚀 Usage methods and examples
- ⚙️ Configuration file templates
- 🔗 CI/CD integration guides

---

## 🔧 Dependency Management Principles

**Important**: These skills are designed to be distribution-friendly:

- ✅ **No forced dependency installation** - Skills only provide guides and scripts
- ✅ **Friendly dependency prompts** - Clear installation suggestions when tools are missing
- ✅ **Flexible execution** - Supports local tools or containerized execution
- ✅ **Multi-environment compatible** - Developers prepare environments as needed

Each skill's `SKILL.md` contains a "Prerequisites" section listing:

- Required tools and minimum versions
- Check commands
- Installation reference links

---

## 🌟 Contributing New Skills

To add a new skill, follow this structure:

```
.agents/skills/
└── your-skill-name/
    ├── SKILL.md          # Main documentation (required, with YAML frontmatter)
    ├── scripts/          # Executable scripts (recommended)
    │   ├── script.ps1    # Windows PowerShell
    │   └── script.sh     # Linux/Mac Bash  
    └── examples/         # Example files (optional)
```

**SKILL.md Format Requirements:**

```markdown
---
name: skill-name
description: Short description (one sentence)
---

# Skill Title

## 📋 Overview
## 🔧 Prerequisites
## 🚀 Usage
## 🎯 What It Checks
## 📊 Output Example
## ⚙️ Configuration
## 🔗 Related Resources
```

---

## 📞 Getting Help

- Check the specific skill's SKILL.md documentation
- Check the script's `--help` option
- Refer to the official documentation links for related tools
