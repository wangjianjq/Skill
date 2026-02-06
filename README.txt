# Agents-MD Pro v7.5 Ultimate — AI-Native Passive Context Development Framework

> **Version**: 7.5.0 Ultimate | **Philosophy**: Zero-Decision Burden & Passive Context
> **Last Audit**: 2026-02-02

---

## Overview

This document is written in Markdown format but maintained as a TXT
file to prevent AI from mistaking it for the main boot file (built-in
rules constrain this, but AI can be forced to read it).

Agents-MD Pro v7.5 is a **Boundary Constraint Framework** for
AI-assisted software development. It systematically mitigates the
"Hallucination" problem in Large Language Models (LLMs) by enforcing
strict protocols that restrict AI behavior to controllable,
predictable ranges. This significantly reduces unpredictable errors and
saves substantial rework time and Token consumption.

### ⭐ Core Value Proposition

| Benefit | Description |
|:---|:---|
| **Reduced Rework** | Makes AI-driven programming (Vibe Coding) controllable and efficient |
| **Eliminated Misunderstanding** | Standardized rules ensure accurate interpretation and execution of user intent |
| **Commercial-Grade Delivery** | Integrated polyglot standards, UI/UX gates, and automated testing for professional output |

---

## ⭐ Project Highlights

> **What makes Agents-MD Pro unique?**

- 🧠 **Passive Context Long-Memory** — Native adapters for 10+ AI tools (Copilot/Cursor/Gemini), ensuring zero-friction rule persistence and effectively mitigating "Rule Amnesia" in long sessions
- 🔒 **Protocol Land Immutability** — Core configurations are read-only, preventing AI corruption
- 🎤 **Personalized Onboarding** — 3-phase handshake interview tailors AI behavior to your skill level
- 🛡️ **Double-Confirmation Safety** — Destructive commands require exact pass-phrase match
- 📐 **50+ Framework Protocols** — Pre-verified rules for mainstream languages and frameworks
  (including WeChat Mini Program, native , React, Vue, Flutter, etc.)
- 🧪 **Sandbox Evolution** — New technologies can be safely tested before official adoption
- 🌍 **Global-First Design** — Automated i18n enforcement for multi-language projects

---

## Core Mechanisms & Features

### 🔍 Passive Context Architecture

The system automatically indexes the project root using a
**high-density compressed tag system** (`AGENTS_INDEX.yaml`),
optimizing the "Long Context Window" for maximum retrieval accuracy
while minimizing token usage.

### 🤖 Hybrid Intelligence & Skills Ecosystem

**"Local Precision + AI Reasoning" — The best of both worlds.**

Agents-MD Pro v7.5 introduces a **Hybrid Usage** model that seamlessly
blends zero-cost local tools with advanced AI capabilities.
This project now natively supports a Skills ecosystem, allowing both
built-in and user-defined Skills to function across any AI environment.

- **Adaptive Execution**:
  The system intelligently routes tasks—simple formatting runs locally
  (0 tokens), while complex logic triggers AI reasoning.

- **Cross-AI Portability**:
  Skills stored in `.agent/skills/` are instantly recognized by
  **Antigravity, Cursor, Windsurf, Claude Code, and Copilot**.

- **User-Extensible**:
  You can easily add your own custom Skills to the ecosystem by
  creating new folders in `.agent/skills/`.

#### 🧰 Built-in Skills Matrix

This project includes **16 Skills** in two categories:

**🔹 Complete Skills (6)** — Includes cross-platform scripts, ready to use  
AI directly invokes local scripts with automatic dependency detection and friendly installation prompts.

**🔸 Guide Skills (10)** — Includes comprehensive documentation  
AI reads documentation, auto-constructs commands, and intelligently handles missing dependencies with installation assistance.

| Skill | Type | Execution | Cost | Description |
|:---|:---|:---|:---|:---|
| **lint-python** | 🔹 Complete | ⚡ Local | $0 | Python code quality check + auto-fix via Ruff |
| **format-python** | 🔹 Complete | ⚡ Local | $0 | Python code formatting via Black |
| **lint-js** | 🔹 Complete | ⚡ Local | $0 | JS/TS code quality check via ESLint |
| **format-js** | 🔹 Complete | ⚡ Local | $0 | JS/TS code formatting via Prettier |
| **ai-agent-lint** | 🔹 Complete | ⚡ Local | $0 | LangChain/AutoGen AI Agent code check |
| **docker-lint** | 🔹 Complete | ⚡ Local | $0 | Dockerfile best practices & security check |
| **security-check** | 🔸 Guide | ⚡ Local | $0 | Scan dependencies for vulnerabilities (npm/pip/multi-lang) |
| **run-tests** | 🔸 Guide | ⚡ Local | $0 | Intelligently executes project test suites |
| **git-commit** | 🔸 Guide | 🧠 AI | Tokens | Generates semantic commits per conventional standards |
| **generate-changelog** | 🔸 Guide | ⚡ Local | $0 | Auto-compiles git history into readable logs |

> **💡 Key Advantage**: Even Guide Skills are AI-powered.  
> Example: When tools are missing, AI proactively asks and executes installation commands—no manual intervention needed.

View full Skills list: [`.agent/skills/index.md`](./.agent/skills/index.md)

#### ⚙️ Local Tool Prerequisites

To unlock the **Zero Token Cost** local execution, ensure these
standard tools are installed:

- **JS/TS Development**: `npm install -g prettier eslint`
- **Python Development**: `pip install black ruff pip-audit`

> **Note**: Without these tools, the system gracefully degrades to AI simulation
> (consuming tokens).


### 🧠 Dynamic Context Injection Protocol (DCIP)

> **"The External Hippocampus" for AI**

Solving the "Lost in the Middle" and "Split-Brain" issues in long-context development.

- **Problem**: AI often forgets early architectural decisions (Refusal to Eval) or hallucinates file structures as projects grow.
- **Solution**: The `make_prompt.py` script acts as an active context assembler.
- **Mechanism**: It constructs a perfect "Sandwich Prompt" by combining:
  1.  **Deep Memory** (Architecture Decision Records from `context/memory.md`)
  2.  **Live State** (Real-time File Tree & Tech Stack from `context/status.md`)
  3.  **User Query** (Your current instruction)
- **Effect**: Ensures AI **never forgets** a past decision and **never hallucinates** a non-existent file.

**Usage**: Run `python make_prompt.py "Your Question"` -> Paste to AI.

### 📐 Regulatory Development Constraints

Includes **Official Stable Specifications** for major programming
languages and frameworks. Pre-verified rules for popular third-party
tools enable seamless, best-practice development.

### 🛡️ Two-Land Doctrine (Territory-Based Access Control)

| Territory | Rights | Description |
|:---|:---|:---|
| 🔴 **Protocol Land** | Read-Only | Core configurations (`.agents/`). AI cannot modify or delete |
| 🟢 **User Land** | Read-Write | All user project files. AI has full authority |
| 🧪 **Sandbox Domain** | Read-Write | Evolution zone for new protocols pending ratification |

### ⚠️ Red Button Rule (Safety Overrides)

Actively intercepts high-risk commands (e.g., `rm -rf /`) with a strict
verification process:

1. **Double Warning**: English + Chinese red-alert notifications
2. **Liability Disclosure**: Explicit responsibility acknowledgment
3. **Exact Pass-Phrase**: Must input **`I-CONFIRM`** or **`我已明确确认`** (no fuzzy matching)

> Any deviation immediately terminates the operation.

### 📋 Lightweight Development Workflow

All AI-assisted development follows this **5-Step Process**
(defined in `PROJECT_GOVERNANCE.md`):

```text
Step 1 → Scope Confirmation
Step 2 → Mini Design (3-7 lines, bilingual encouraged)
Step 3 → Implementation (following .agents/ rules)
Step 4 → Self-Testing (logic validation + test cases)
Step 5 → Documentation Update (CHANGELOG.md required)
```

### 🤝 Personalized User Interview

First-time users undergo a **3-Phase Handshake Interview** to establish
their developer persona:

| Phase | Purpose |
|:---|:---|
| **Experience Assessment** | Determine overall proficiency level (Novice to Expert) |
| **Tech Stack Matrix** | Rate familiarity with specific technologies (1-5 scale) |
| **Collaboration Style** | Choose: Interactive Tutor / Silent Pro / On-Demand |

Results are stored in `USER_PROFILE.md` for tailored AI assistance
throughout the project lifecycle.

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

Mandates maintenance of `PROJECT_LANGUAGES.md`. The system automatically
guides multi-language adaptation, ensuring features and content are
ready for global deployment.

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

```text
Agents-MD-Pro/
├── 📄 AGENTS.md              # Master boot file (AI entry point)
├── 📄 AGENTS_INDEX.yaml      # High-density compressed knowledge index
├── 📄 PROJECT_GOVERNANCE.md  # Development workflow & rules
├── 📄 PROJECT_STATUS.md      # Current project governance state & skeleton
├── 📄 USER_PROFILE.md        # User persona & preferences
├── 📄 PROJECT_LANGUAGES.md   # i18n allowed languages list
├── 📄 CONVENTIONS.md         # Project-specific coding conventions
├── 📄 CHANGELOG.md           # Auto-maintained change log
├── 📄 README.txt             # English documentation
├── 📄 README_zh-CN.txt       # Chinese documentation
├── 📄 replit.md              # Replit environment configuration
│
├── 🤖 CLAUDE.md              # Claude Code CLI adapter
├── 🤖 GEMINI.md              # Gemini CLI adapter
├── 🤖 QWEN.md                # Qwen Code CLI adapter
├── 🤖 .cursorrules           # Cursor adapter
├── 🤖 .windsurfrules         # Windsurf adapter
├── 🤖 .clinerules            # Cline (VS Code) adapter
├── 🤖 .augment-guidelines    # Augment Code adapter
├── 🤖 .aider.conf.yml        # Aider CLI configuration
│
├── 🔧 setup.bat / setup.sh   # Environment bootstrap
├── 🔧 ResetAG.bat / .sh      # Protocol reset tools (State clearing)
│
├── 📁 .agents/               # 🔴 Protocol Land (Core Rules - Read-Only)
├── 📁 .agent/                # 🟠 Workflow definitions & Skills
├── 📁 .gemini/               # 🧠 Agent Brain & Memory (DO NOT DELETE)
├── 📁 .github/               # 🐙 GitHub Copilot adapter
├── 📁 .idea/                 # 🧩 JetBrains AI adapter
├── 📁 .zed/                  # 🧩 Zed AI adapter
├── 📁 .codex/                # 🧩 Codex CLI (OpenAI) adapter
└── 📁 bmad/                  # 🟢 BMAD-Method Runtime
```

### File Categories

| Category | File | Description |
|:---|:---|:---|
| **Entry Point** | `AGENTS.md` | AI reads this first. Contains boot sequence & core rules |
| **Knowledge Index** | `AGENTS_INDEX.yaml` | Compressed path map for passive context retrieval |
| **Governance** | `PROJECT_GOVERNANCE.md` | 5-step workflow, CHANGELOG rules, Mini Design template |
| **State Tracking** | `PROJECT_STATUS.md` | Tracks governance mode, tech stack, and refactor status |
| **User Profile** | `USER_PROFILE.md` | Stores developer persona (Expert/Novice) and preferences |
| **i18n Config** | `PROJECT_LANGUAGES.md` | Defines supported languages for global-first development |
| **Coding Style** | `CONVENTIONS.md` | Project-specific coding standards and patterns |
| **Documentation** | `README.txt` / `README_zh-CN.txt` | Bilingual project documentation (Human Facing) |
| **Change Log** | `CHANGELOG.md` | AI-maintained bilingual change history |
| **CLI Adapters** | `CLAUDE.md`, `GEMINI.md`, `QWEN.md` | Auto-context loaders for CLI tools |
| **IDE Adapters** | `.cursorrules`, `.windsurfrules`, etc. | Auto-context loaders for IDEs/editors |
| **Environment** | `setup.bat` / `setup.sh` | Install dependencies (uv, node) |
| **Reset** | `ResetAG.bat` / `ResetAG.sh` | Clear state files for re-initialization |
| **Agent Memory** | `.gemini/` | Critical agent state storage. **Delete = Agent Amnesia** |
| **Framework** | `.agents/` | Core definition files for languages, frameworks, and skills |
| **Workflows** | `.agent/` | Executable workflows and skill scripts |

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

Copy all files from this project (not the extracted directory itself)
to your project's **Root Directory**, ensuring that all files and
subdirectories from this project appear directly in your project's
root directory.

> ⚠️ **Critical**: Do not place in subdirectories or indexing will fail.

### 2. Environment Check (Optional)

| Platform | Command |
|:---|:---|
| Windows | `setup.bat` |
| Linux/macOS | `sh setup.sh` |

> Scripts automatically check the environment and install recommended
> tools like `uv`. If Node.js v20+ is not available, the system will
> automatically downgrade to the built-in solution, but performance
> will not significantly degrade.

### 3. Governance Mode Selection

Upon first run (no `PROJECT_STATUS.md`), the AI will prompt for a mode:

| Mode | Description |
|:---|:---|
| **[1] Strict Refactor** | Reorganize files to match Agents-MD protocol |
| **[2] Progressive** ⭐ | Apply new specs while preserving existing files (Recommended) |
| **[3] Legacy** | Follow existing project style |

> To re-initialize at any time, run `ResetAG.bat` (Win) or
> `ResetAG.sh` (Unix).

### 4. Start Developing

The AI will automatically read `AGENTS.md` and load the constraint rules.
However, it is still strongly recommended that you explicitly instruct
the AI to read the `AGENTS.md` file first.

---

## Quick Commands

| Command | Function | When to Use |
|:---|:---|:---|
| `/rrrr` | Refresh Context | New session, or when AI "forgets" rules after long conversations |
| `/aaaa` | View AGENTS.md | When you need to review project governance rules |

> **Tip**: If AI behavior deviates from expectations, type `/rrrr` to reload all governance files.

---

## Supported AI Tools

This project includes adapters for the following mainstream AI coding tools.
Each tool will **automatically load** its corresponding config file when opening the project:

### 🖥️ AI IDEs / Editors

| Tool | Config File | Status |
|:---|:---|:---|
| **Google Antigravity** | `.agent/rules/`, `GEMINI.md` | ✅ Supported |
| **Cursor** | `.cursorrules` | ✅ Supported |
| **Windsurf** | `.windsurfrules` | ✅ Supported |
| **GitHub Copilot** | `.github/copilot-instructions.md` | ✅ Supported |
| **JetBrains AI** | `.idea/ai-instructions.md` | ✅ Supported |
| **Cline (VS Code)** | `.clinerules` | ✅ Supported |
| **Augment Code** | `.augment-guidelines` | ✅ Supported |
| **Zed AI** | `.zed/ai.md` | ✅ Supported |

### 💻 CLI Tools

| Tool | Config File | Status |
|:---|:---|:---|
| **Claude Code** | `CLAUDE.md` | ✅ Supported |
| **Gemini CLI** | `GEMINI.md`, `.gemini/` | ✅ Supported |
| **Aider** | `.aider.conf.yml`, `.aiderignore` | ✅ Supported |
| **Codex CLI (OpenAI)** | `.codex/instructions.md` | ✅ Supported |
| **Qwen Code** | `QWEN.md` | ✅ Supported |

> **How it works**: Each adapter file contains a "Read `AGENTS.md` first" directive,
> ensuring AI automatically loads project governance rules in every new session.

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

BMad is an AI-driven agile framework featuring 21+ specialized agents
and 50+ guided workflows. It supports the **/bmad-help** command and
includes a "Party Mode" for multi-agent collaboration.


### About Vercel's Passive Context

| Concept | Description |
|:---|:---|
| **Passive Injection** | Implants indexes into system prompts to avoid tool-call overhead |
| **Retrieval-First** | Guides AI to refer to live docs over outdated training data |
| **Compressed Indexing** | High-precision path maps within an 8KB footprint |

---

> By using Agents-MD Pro v7.5, developers gain a **secure, standardized,
> and high-quality** AI collaboration environment, ensuring professional
> results from prototype to production.
