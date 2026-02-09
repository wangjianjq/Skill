
# Agents-MD Pro v7.5 Ultimate — AI-Native Passive Context Development Framework

> **Version**: 7.5.0 Ultimate | **Philosophy**: Zero-Decision Burden & Passive Context
> **Last Audit**: 2026-02-02

---

## Overview

Agents-MD Pro v7.5 is a **Boundary Constraint Framework** for AI-assisted software development. It systematically mitigates the "Hallucination" problem in Large Language Models (LLMs) by enforcing strict protocols that restrict AI behavior to controllable, predictable ranges.

### ⭐ Core Value Proposition

| Benefit | Description |
|:---|:---|
| **Reduced Rework** | Makes AI-driven programming (Vibe Coding) controllable and efficient |
| **Eliminated Misunderstanding** | Standardized rules ensure accurate interpretation and execution of user intent |
| **Commercial-Grade Delivery** | Integrated polyglot standards, UI/UX gates, and automated testing for professional output |

---

## ⭐ Project Highlights

> **What makes Agents-MD Pro unique?**

- 🔒 **Protocol Land Immutability** — Core configurations are read-only, preventing AI corruption
- 🎤 **Personalized Onboarding** — 3-phase handshake interview tailors AI behavior to your skill level
- 🛡️ **Double-Confirmation Safety** — Destructive commands require exact pass-phrase match
- 📐 **50+ Framework Protocols** — Pre-verified rules for mainstream languages and frameworks (including WeChat Mini Program, React, Vue, Flutter, etc.)
- 🧪 **Sandbox Evolution** — New technologies can be safely tested before official adoption
- 🌍 **Global-First Design** — Automated i18n enforcement for multi-language projects

---

## Core Mechanisms & Features

### 🔍 Passive Context Architecture

The system automatically indexes the project root using a **high-density compressed tag system** (`AGENTS_INDEX.yaml`), optimizing the "Long Context Window" for maximum retrieval accuracy while minimizing token usage.

### 🤖 Hybrid Intelligence & Skills Ecosystem

**"Local Precision + AI Reasoning" — The best of both worlds.**

Agents-MD Pro v7.5 introduces a **Hybrid Usage** model that seamlessly blends zero-cost local tools with advanced AI capabilities. This project now natively supports a Skills ecosystem, allowing both built-in and user-defined Skills to function across any AI environment.

- **Adaptive Execution**: The system intelligently routes tasks—simple formatting runs locally (0 tokens), while complex logic triggers AI reasoning.
- **Cross-AI Portability**: Skills stored in `.agent/skills/` are instantly recognized by **Antigravity, Cursor, Windsurf, Claude Code, and Copilot**.
- **User-Extensible**: You can easily add your own custom Skills to the ecosystem by creating new folders in `.agent/skills/`.

#### 🧰 Built-in Skills Matrix

| Skill | Execution | Cost | Description |
|:---|:---|:---|:---|
| **format-js / python** | ⚡ Local | $0 | Millisecond-level code formatting via Prettier/Black |
| **lint-js / python** | ⚡ Local | $0 | Static analysis and auto-fixing via ESLint/Ruff |
| **security-check** | ⚡ Local | $0 | Scans dependencies for vulnerabilities (npm/pip) |
| **run-tests** | ⚡ Local | $0 | Intelligently executes project test suites |
| **git-commit** | 🧠 AI | Tokens | Generates semantic commits based on conventional standards |
| **generate-changelog** | ⚡ Local | $0 | Auto-compiles git history into human-readable logs |

#### ⚙️ Local Tool Prerequisites

To unlock the **Zero Token Cost** local execution, ensure these standard tools are installed:

- **JS/TS**: `npm install -g prettier eslint`
- **Python**: `pip install black ruff pip-audit`

> **Note**: Without these tools, the system gracefully degrades to AI simulation (consuming tokens).

### 📐 Regulatory Development Constraints

Includes **Official Stable Specifications** for major programming languages and frameworks. Pre-verified rules for popular third-party tools enable seamless, best-practice development.

### 🛡️ Two-Land Doctrine (Territory-Based Access Control)

| Territory | Rights | Description |
|:---|:---|:---|
| 🔴 **Protocol Land** | Read-Only | Core configurations (`.agents/`). AI cannot modify or delete |
| 🟢 **User Land** | Read-Write | All user project files. AI has full authority |
| 🧪 **Sandbox Domain** | Read-Write | Evolution zone for new protocols pending ratification |

### ⚠️ Red Button Rule (Safety Overrides)

Actively intercepts high-risk commands (e.g., `rm -rf /`) with a strict verification process:

1. **Double Warning**: English + Chinese red-alert notifications
2. **Liability Disclosure**: Explicit responsibility acknowledgment
3. **Exact Pass-Phrase**: Must input **`I-CONFIRM`** or **`我已明确确认`** (no fuzzy matching)

> Any deviation immediately terminates the operation.

### 📋 Lightweight Development Workflow

All AI-assisted development follows this **5-Step Process** (defined in `PROJECT_GOVERNANCE.md`):

```
Step 1 → Scope Confirmation
Step 2 → Mini Design (3-7 lines, bilingual encouraged)
Step 3 → Implementation (following .agents/ rules)
Step 4 → Self-Testing (logic validation + test cases)
Step 5 → Documentation Update (CHANGELOG.md required)
```

### 🤝 Personalized User Interview

First-time users undergo a **3-Phase Handshake Interview** to establish their developer persona:

| Phase | Purpose |
|:---|:---|
| **Experience Assessment** | Determine overall proficiency level (Novice to Expert) |
| **Tech Stack Matrix** | Rate familiarity with specific technologies (1-5 scale) |
| **Collaboration Style** | Choose: Interactive Tutor / Silent Pro / On-Demand |

Results are stored in `USER_PROFILE.md` for tailored AI assistance throughout the project lifecycle.

### 🧪 Full-Stack Polyglot QA & Testing

Covers **Python, Node.js, Go, C++, Java, Mobile**, and 11+ other stacks with:
- Standardized test workflows
- Automated unit/integration test prompts
- Structured logging mandates (raw `print()` forbidden in production)

### 🎨 Professional UI/UX Design Standards

Integrated **"Design Gate"** protocol enforcing modern aesthetics:
- Glassmorphism & Depth effects
- Bento UI (Grid) organization
- Professional Iconography (Lucide / Heroicons)
- 4px grid spacing system
- Dark mode strategy (CSS Variables)

### 🌍 Automated i18n Protocol

Mandates maintenance of `PROJECT_LANGUAGES.md`. The system automatically guides multi-language adaptation, ensuring features and content are ready for global deployment.

### 🏗️ Architectural Governance

Enforces structural rigor through `SKILL_ARCHITECT` protocol:
- **SOLID Principles**: Mandatory Single Responsibility and Open-Closed compliance
- **Dependency Rule**: Inner layers must not depend on outer layers
- **Technical Debt Tracking**: No "God Objects"; bounded contexts required
- **Design Pattern Toolkit**: Factory, Strategy, Observer, Adapter recommendations

### 📝 Structured Debugging Standards

| Rule | Enforcement |
|:---|:---|
| **FORBIDDEN** | Raw `print()` / `console.log()` in production code |
| **REQUIRED** | Platform-standard structured logging with timestamps and levels |
| **AUTOMATED** | Test prompts after feature completion |

---

## Project Structure

### Directory Tree

```
Agents-MD-Pro/
├── 📄 AGENTS.md              # Master boot file (AI entry point)
├── 📄 AGENTS_INDEX.yaml      # High-density compressed knowledge index
├── 📄 PROJECT_GOVERNANCE.md  # Development workflow & rules
├── 📄 CHANGELOG.md           # Auto-maintained change log
├── 📄 README.txt             # English documentation
├── 📄 README_zh-CN.txt       # Chinese documentation
│
├── 🔧 setup.bat / setup.sh   # Environment bootstrap scripts
├── 🔧 ResetAG.bat / .sh      # Protocol reset tools
├── 🔧 .cursorrules           # IDE integration (Cursor, Antigravity, VS Code plugins, and various CLI tools like Claude Code, Gemini CLI, OpenCode, etc.)
│
├── 📁 .agents/               # 🔴 Protocol Land (Read-Only)
│   ├── 📁 lang/              # Language protocols (C, Python, Go, Rust...)
│   ├── 📁 frameworks/        # Framework protocols (React, Vue, FastAPI...)
│   ├── 📁 database/          # Database protocols (PostgreSQL, MongoDB...)
│   ├── 📁 cloud/             # Cloud platform protocols (AWS, GCP, Azure)
│   ├── 📁 skills/            # Skill modules (Onboarding, Debugging, i18n...)
│   ├── 📁 knowledge/         # Domain knowledge base
│   └── 📁 sandbox/           # 🧪 Sandbox for experimental protocols
│
├── 📁 .agent/                # Workflow definitions
│   └── 📁 workflows/         # 40+ BMAD workflow scripts
│
└── 📁 bmad/                  # BMAD-Method runtime (optional, 219 files)
```

### File Categories

| Category | File | Description |
|:---|:---|:---|
| **Entry Point** | `AGENTS.md` | AI reads this first. Contains boot sequence & core rules |
| **Knowledge Index** | `AGENTS_INDEX.yaml` | Compressed path map for passive context retrieval |
| **Governance** | `PROJECT_GOVERNANCE.md` | 5-step workflow, CHANGELOG rules, Mini Design template |
| **Documentation** | `README.txt` / `README_zh-CN.txt` | Bilingual project documentation |
| **Change Log** | `CHANGELOG.md` | AI-maintained bilingual change history |
| **Environment** | `setup.bat` / `setup.sh` | Install dependencies (uv, Node.js check) |
| **Reset** | `ResetAG.bat` / `ResetAG.sh` | Clear state files for re-initialization |
| **IDE Integration** | `.cursorrules` | Multi-IDE integration rules (Cursor, Antigravity, VS Code, CLI tools, etc.) |

### Protocol Directories

| Directory | Content | Count |
|:---|:---|:---|
| `.agents/lang/` | Language protocols | 10+ |
| `.agents/frameworks/` | Framework protocols (React, Vue, FastAPI, **WeChat Mini Program**...) | 50+ |
| `.agents/database/` | Database protocols | 6+ |
| `.agents/cloud/` | Cloud platform protocols | 3+ |
| `.agents/skills/` | Skill modules (Onboarding, Debug, i18n...) | 18+ |
| `.agents/knowledge/` | Domain knowledge (Design, QA...) | 5+ |
| `.agents/sandbox/` | Experimental protocols | Variable |
| `.agent/workflows/` | BMAD workflow scripts | 40 |
| `bmad/` | BMAD-Method runtime | 219 |

---

## Supported Tech Stack

| Category | Framework / Language |
|:---|:---|
| **System** | C, C++ (Modern), Rust, Zig |
| **Backend** | Python (FastAPI/Flask), Go, Java, Node.js (TypeScript), C# (.NET Core) |
| **Frontend** | React (Vite/Next.js), Vue 3, Angular, TailwindCSS |
| **Mobile** | Swift (iOS), Kotlin (Android), React Native, Flutter |
| **Embedded** | Arduino, ESP-IDF, Zephyr RTOS, FreeRTOS |
| **Wireless** | BLE (nRF Sniffer), LoRa, USB Protocol Analysis |
| **Instruments** | R&S CMW500, Keysight UXM 5G, Anritsu MT8821C, Tektronix Scope, Saleae Logic, etc. |

---

## Quick Start

### 1. Deployment

Copy all files from this project (not the extracted directory itself) to your project's **Root Directory**, ensuring that all files and subdirectories from this project appear directly in your project's root directory.

> ⚠️ **Critical**: Do not place in subdirectories or indexing will fail.

### 2. Environment Check (Optional)

| Platform | Command |
|:---|:---|
| Windows | `setup.bat` |
| Linux/macOS | `sh setup.sh` |

> Scripts automatically check the environment and install recommended tools like `uv`. If Node.js v20+ is not available, the system will automatically downgrade to the built-in solution, but performance will not significantly degrade.

### 3. Governance Mode Selection

Upon first run (no `PROJECT_STATUS.md`), the AI will prompt for a mode:

| Mode | Description |
|:---|:---|
| **[1] Strict Refactor** | Reorganize files to match Agents-MD protocol |
| **[2] Progressive** ⭐ | Apply new specs while preserving existing files (Recommended) |
| **[3] Legacy** | Follow existing project style |

> To re-initialize at any time, run `ResetAG.bat` (Win) or `ResetAG.sh` (Unix).

### 4. Start Developing

The AI will automatically read `AGENTS.md` and load the constraint rules. However, it is still strongly recommended that you explicitly instruct the AI to read the AGENTS.md file first.

---

## Important Notes

| Note | Description |
|:---|:---|
| **Conflict Protection** | If a `bmad` folder exists, the system uses `_bmad` for runtime data |
| **Resource Shielding** | AI ignores this README by default to save context tokens |
| **Mandatory Boot Sequence** | AI **must** execute Boot Sequence before processing any development request |
| **Version Sovereignty** | For legacy projects, AI reads manifests (`package.json`, `go.mod`) to select appropriate protocol rules |

---

## Acknowledgments

This project is inspired by and built upon the following initiatives:

- **Vercel Research** (Agents.md Architecture)
  Theoretical foundation for Passive Context development.
  [https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)

- **BMAD-METHOD**
  Core logic for automated specifications and bootstrap management.
  [https://github.com/bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)

---

## Extension Reading

### About BMad-Method

An AI-driven agile framework featuring 21+ specialized agents and 50+ guided workflows. Supports the **/bmad-help** command and "Party Mode" for multi-agent collaboration.

### About Vercel's Passive Context

| Concept | Description |
|:---|:---|
| **Passive Injection** | Implants indexes into system prompts to avoid tool-call overhead |
| **Retrieval-First** | Guides AI to refer to live docs over outdated training data |
| **Compressed Indexing** | High-precision path maps within an 8KB footprint |

---

> By using Agents-MD Pro v7.5, developers gain a **secure, standardized, and high-quality** AI collaboration environment, ensuring professional results from prototype to production.
