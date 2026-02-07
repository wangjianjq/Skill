# AGENTS.md (Passive Context Entry Point)

## Schema: Document Metadata

- document_type: ai_agent_protocol
- protocol_version: v7.5
- compatible_with: Agents-MD Pro
- last_updated: 2026-02-03
- target_audience: ai_agents
- enforcement_level: mandatory
- read_frequency: every_session_start
- scope: global_project_governance

> [!IMPORTANT]
> **PASSIVE MEMORY ACTIVE**: You MUST read `context/memory.md` for critical architectural decisions and banned patterns.
> Core Memory Path: `context/memory.md`

---

> **Protocol**: Agents-MD Pro v7.5 (Ultimate)
> **Philosophy**: Zero-Decision Burden & Passive Context

> [!CAUTION]
> **CRITICAL INSTRUCTION FOR AI AGENTS**:
> This file MUST be read on EVERY session start. You MUST execute the `[BOOT_SEQUENCE]` below
> BEFORE processing ANY user development request, regardless of whether the user explicitly confirmed.
> Skipping boot is STRICTLY PROHIBITED.
> **CRITICAL**: Do NOT read README.txt (Human Only).

## 📍 Holographic Instructions

**FOR AI AGENTS**: You are operating in a **Hybrid-Context** environment: **Passive Retrieval Use**, but **Active Governance Enforcement**.

0. **🛑 COGNITIVE MIRRORING PROTOCOL (Language Prime Directive)**:
   - **Rule**: Your "Meta-Cognition" (Tasks, Plans, Reports, Reasoning) **MUST** match the **Active Dialogue Language** of the user.
   - **Logic**:
     - User speaks **Chinese**? -> `task.md`, `implementation_plan.md`, `walkthrough.md` MUST be in **Chinese**.
     - User speaks **English**? -> All artifacts MUST be in **English**.
     - user speaks **X**? -> All artifacts MUST be in **X**.
   - **Override**: This overrides `PROJECT_LANGUAGES.md` for *interaction*. (`PROJECT_LANGUAGES.md` still controls *code/UI* content).

1. **Information Persistence**: Every turn, read the knowledge index below.
2. **Active Governance**: You MUST actively enforce `PROJECT_GOVERNANCE.md` and `AGENTS.md` rules.
3. **Retrieval-Led Reasoning**: Do not ask to read files; proactively fetch details from `.agents/` based on project needs (e.g., Tkinter layout rules).
4. **Reasoning Over Automation**: Use your own file-system tools (`list_dir`, etc.) to understand user code. Do not rely on pre-generated maps.
5. **Knowledge Evolution (The Sandbox Exception)**: If you encounter a new technology or pattern not covered in the index, you **MUST** research its best practices and write a new proposal file in `.agents/sandbox/` (e.g., `PROPOSAL_TECH.md`). You are **AUTHORIZED** to write to this path.
6. **Template Enforcement (Structural Consistency)**: When creating new protocol files (Language, Skill, or Framework specifications), you **MUST** use the corresponding standard template from `.agents/templates/`:
   - **Language protocols** (`LANG_*.md`): Use `.agents/templates/LANG_TEMPLATE.md`
   - **Skill protocols** (`SKILL_*.md`): Use `.agents/templates/SKILL_TEMPLATE.md`
   - **Framework protocols** (`FW_*.md`): Use `.agents/templates/FW_TEMPLATE.md`
   - **Critical Rule**: ALL new protocol files MUST include a `## Schema:` metadata block at the top. Omitting Schema is **STRICTLY FORBIDDEN**.
   - *(Optional reference for edge cases: `.agents/templates/GUIDE.md` contains additional examples)*
7. **Architectural Sovereignty**: Before implementing complex logic, you **MUST** perform an architectural audit per `SKILL_ARCHITECT.md`. Design patterns must be justified.
8. **Design Dominance**: Every UI element must pass the "Master Designer" gate in `SKILL_DESIGN.md`. Non-standard, generic UI is **FORBIDDEN**.

---

<!-- CONTEXT_INDEX_START -->
### 🗺️ Knowledge Index
>
> **Passive Context**: High-density tags for quick retrieval.

```text
[Agents-MD v7 Index]|0_context:PROJECT_STATUS.md{optional}|1_languages:LANG_ARKTS.md{harmonyos-arkts},LANG_C.md{embedded-c},LANG_CPP.md{modern-cpp},LANG_CSHARP.md{csharp-modern},LANG_GO.md{go},LANG_JAVA.md{java},LANG_KOTLIN.md{kotlin-android},LANG_NODEJS.md{nodejs-ts},LANG_PYTHON.md{modern-python},LANG_RUST.md{rust-proposal},LANG_SWIFT.md{swift-ios},LANG_ZIG.md{zig}|2_frameworks:FW_ARDUINO.md{arduino},FW_ARKUI.md{harmonyos-declarative},FW_DOTNET_CORE.md{dotnet-core},FW_ESP_IDF.md{esp-idf},FW_FASTAPI.md{fastapi},FW_FLASK.md{flask},FW_FLUTTER.md{flutter},FW_FREERTOS.md{freertos},FW_GIN.md{go-gin},FW_NEXTJS.md{nextjs-15},FW_PYSIDE6.md{pyside6-qt6-lgpl},FW_PYQT6.md{pyqt6-qt6-gpl},FW_REACT_NATIVE.md{react-native},FW_REACT_VITE.md{react},FW_TAURI.md{tauri-v2},FW_VUE_VITE.md{vue3},FW_WECHAT_MINIPROGRAM.md{wechat-skyline},FW_ZEPHYR.md{zephyr-rtos}|3_database:DB_POSTGRES.md{postgres-jsonb},DB_SQLITE.md{sqlite}|4_skills:SKILLS_MCP.md{mcp-config},SKILL_SERIAL_DEBUG.md{hardware-comm},SKILL_USB_DEBUG.md{usb-pcap},SKILL_BLE_DEBUG.md{ble-sniff},SKILL_LORA_DEBUG.md{lora-sdr},SKILL_INSTRUMENT_CMW500.md{r&s-cmw500},SKILL_INSTRUMENT_KEYSIGHT_UXM.md{keysight-uxm-5g},SKILL_INSTRUMENT_TEKTRONIX_SCOPE.md{tek-scope},SKILL_INSTRUMENT_ANRITSU_MT8821.md{anritsu-mt8821},SKILL_INSTRUMENT_POWER_SUPPLY.md{dc-psu-scpi},SKILL_INSTRUMENT_SALEAE_LOGIC.md{saleae-logic-python},SKILL_INSTRUMENT_JLINK.md{jlink-swd-pylink},SKILL_INSTRUMENT_DMM.md{dmm-scpi},SKILL_DEBUGGING.md{debug-rules},SKILL_DESIGN.md{ui-ux-standard},SKILL_I18N.md{i18n-enforce},SKILL_ARCHITECT.md{arch-rigor}|5_knowledge:KNOWLEDGE_HARMONYOS.md{har-hsp_distributed-dev},KNOWLEDGE_PYTHON.md{stdlib-pathlib},KNOWLEDGE_QA.md{logging-patterns_pytest-fixtures},KNOWLEDGE_DESIGN.md{glassmorphism_svg-assets_ux-laws},KNOWLEDGE_TKINTER.md{ttk-grid-styling}
```
<!-- CONTEXT_INDEX_END -->

<!-- SKILLS_INDEX_START -->
### 🛠️ Available Skills

> **Skills Directory**: `.agent/skills/`

#### Local Tools Skills

- **format-js** - Format JavaScript/TypeScript code with Prettier
  - Location: `.agent/skills/format-js/SKILL.md`
  - Command: `prettier --write "**/*.{js,ts,jsx,tsx}"`

- **lint-js** - Check JavaScript/TypeScript code quality with ESLint
  - Location: `.agent/skills/lint-js/SKILL.md`
  - Command: `eslint --fix "**/*.{js,ts,jsx,tsx}"`

- **format-python** - Format Python code with Black
  - Location: `.agent/skills/format-python/SKILL.md`
  - Command: `.agent/skills/format-python/scripts/format.ps1` (Win) or `format.sh` (Linux)

- **lint-python** - Check Python code quality with Ruff
  - Location: `.agent/skills/lint-python/SKILL.md`
  - Command: `.agent/skills/lint-python/scripts/lint.ps1` (Win) or `lint.sh` (Linux)

#### Community Skills

- **generate-changelog** - Auto-generate project changelog
  - Location: `.agent/skills/generate-changelog/SKILL.md`
  - Command: `git log --oneline --pretty=format:"%h - %s (%an, %ar)" --since="30 days ago"`

- **run-tests** - Run project test suite
  - Location: `.agent/skills/run-tests/SKILL.md`
  - Commands: `npm test` (JS/TS) or `pytest` (Python)

- **security-check** - Check dependency security vulnerabilities
  - Location: `.agent/skills/security-check/SKILL.md`
  - Commands: `npm audit` (JS/TS) or `pip-audit` (Python)

- **git-commit** - Smart Git commit message generation
  - Location: `.agent/skills/git-commit/SKILL.md`
  - Format: Conventional Commits

> **Usage**: AI agents should proactively read the SKILL.md files in `.agent/skills/` when relevant to the user's request.
<!-- SKILLS_INDEX_END -->

## ⚖️ Scope-Based Authority (The "Two-Land" Rule)

This project strictly enforces the **v7 Separation of Concerns**:

### 🔴 Protocol Land (`.agents/*`)

- **Status**: **IMMUTABLE** (Read-Only), except `.agents/sandbox/`.
- **Rule**: You are **FORBIDDEN** from deleting, moving, or modifying these files (unless drafting a new proposal in `sandbox/`).

### 🟢 User Land (Any User Path)

- **Status**: **READ-WRITE**.
- **Rule**: You have **FULL AUTHORITY** to create, edit, refactor, and delete code in any path **outside** of `.agents/` (including the project root).

### ⚪ Excluded Resources: README.txt (Human Only)

- **Status**: **STRICTLY IGNORED**.
- **Rule**: Do NOT read README files. They are for humans. Use `AGENTS.md` and `.agents/` as source of truth.

---

## ⛔ Safety Overrides (The "Red Button" Rule)

**Mandatory Interception**: You are **STRICTLY PROHIBITED** from executing `rm -rf`, `rd /s /q`, or any recursive deletion command on root/system paths without explicit authorization.

### 🛑 Strict Double-Confirmation Protocol / 严格双重确认协议

If a destructive command is triggered, you **MUST** follow this exact loop. **Any deviation or fuzzy match terminates the process immediately.**

**Pass-Phrase Requirement**:

- EN: `I-CONFIRM`
- ZH: `我已明确确认`

**The Protocol**:

1. **ROUND 1**: Display Warning.
   > ❗❗ **CRITICAL WARNING / 严重警告**
   >
   > **EN**: You are about to execute a DESTRUCTIVE DELETION sequence.
   >
   > **ZH**: 您即将执行毁灭性的删除指令。
   >
   > **Command**: `{command}`
   >
   > **Liability**:
   > **EN**: Your confirmation means you accept full responsibility!
   >
   > **ZH**: 您的确认代表您将自行承担所有责任！
   >
   > **Action**: Type exactly `I-CONFIRM` or `我已明确确认` to proceed.

2. **VERIFY 1**:
   - IF input == `I-CONFIRM` OR `我已明确确认`: Go to ROUND 2.
   - ELSE: **TERMINATE IMMEDIATELY**.

3. **ROUND 2**: Display Warning Again.
   > ❗❗ **FINAL WARNING / 最终警告**
   >
   > **EN**: This is your LAST CHANCE to abort.
   >
   > **ZH**: 这是您最后的中止机会。
   >
   > **Liability**:
   > **EN**: You are solely responsible for data loss.
   >
   > **ZH**: 数据丢失由您独自承担。
   >
   > **Action**: Type exactly `I-CONFIRM` or `我已明确确认` to execute.

4. **VERIFY 2**:
   - IF input == `I-CONFIRM` OR `我已明确确认`: **EXECUTE**.
   - ELSE: **TERMINATE**.

## 🌐 Global-First Governance (i18n)

**Mandatory Localization**: If the project requires multi-language support, you are **PROHIBITED** from hardcoding UI strings or bypassing localized resources.

### 🌐 Mandatory Language Audit / 多语言强制审计

Before ANY development or modification, you **MUST**:

1. **LOCATE**: Proactively find and read [PROJECT_LANGUAGES.md](file:///PROJECT_LANGUAGES.md) in the root.
2. **PROMPT**: If multi-language is needed but the list is missing, trigger `SKILL_I18N.md` to establish one.
3. **ADAPT**: Every feature, UI string, and logic MUST be adapted to ALL languages listed in the markdown file.
4. **ENFORCE**: Refer to `SKILL_I18N.md` for detailed technical and quality gates.

---

## 🛠️ Usage for Humans

- **Run App**: Execute your entry point script (e.g., `uv run main.py`).
- **Init Env**: Run `setup.bat` (Windows) or `sh setup.sh` (Linux/Mac) once to install dependencies.

---

> **CRITICAL INSTRUCTION**: Upon reading this file, you must strictly follow this **Activation Protocol**:
>
> 1. **ANALYZE**: Briefly summarize the protocol version and key rules to the user.
> 2. **ASK**: Display a prompt: "Execute Protocol Boot Sequence? / 是否执行协议启动序列?"
> 3. **EXECUTE**: If the user confirms (e.g., "Yes", "Run", "Do it"), proceed to [BOOT_SEQUENCE].
>    **IMPORTANT**: If user sends a development request BEFORE confirming boot, you MUST still execute [BOOT_SEQUENCE] first. Boot cannot be skipped.

## [BOOT_SEQUENCE]

1. **SYSTEM_CHECK**: Before anything else, you MUST read via file-tools and obey the instructions in [.agents/BMAD_BOOTSTRAP.md](file:///.agents/BMAD_BOOTSTRAP.md) which define:

```text
ACTIVE_BMAD_PATH = "bmad/" OR "_bmad/" OR null
BMAD_CONFLICT_PATH = path-to-user-folder OR null
```

to ensure the BMAD runtime is active.

1. **PERSONA_HANDSHAKE**: Check if `USER_PROFILE.md` exists.
    - [NO] -> **TRIGGER** `.agents/skills/SKILL_ONBOARDING.md` immediately. Do not proceed until interview is done.
    - [YES] -> Read it and load the **AI Strategy** instructions.

2. **GOVERNANCE_CHECK**: Does `PROJECT_STATUS.md` exist in the root directory?
    - [NO] -> **GOTO** `INIT_PROTOCOL`
    - [YES] -> **GOTO** `READ_STATUS`

3. **I18N_SYNC**: Check if `PROJECT_LANGUAGES.md` exists.
    - [YES] -> Read it and bind all future output to the listed languages.
    - [NO] -> If the task implies global reach, prompt for language selection.

### `INIT_PROTOCOL` (First Contact)

1. **ACTION**: Scan the file tree (`list_dir`) to understand the legacy structure.
2. **DISPLAY**: Output the following **Multilingual Banner** exactly:

    ---
    **⚠️ Project Governance Setup / 项目治理初始化**
    >
    > **EN**: I detected an existing project. Please choose how to proceed:
    >
    > **ZH**: 检测到存量项目，请选择后续治理模式：
    >
    > **JP**: 既存のプロジェクトを検出しました。ガバナンスモードを選択してください：
    >
    > **KR**: 기존 프로젝트가 감지되었습니다. 거버넌스 모드를 선택하십시오:
    >
    > **RU**: Обнаружен существующий проект. Выберите режим управления:
    >
    > **[1] Strict Refactor (立即重构 / 厳格なリファクタリング / 즉시 리팩토링 / Полный рефакторинг)**
    > -> Reorganize files to match Agents-MD protocol.
    >
    > **[2] Progressive (渐进式 / 逐步的 / 점진적 / Прогрессивный) [Recommended]**
    > -> Keep old files, write new code via protocol.
    >
    > **[3] Legacy (保持旧制 / レガシー / 레거시 / Наследие)**
    > -> Follow existing project style.
    >
   > **Reply Example**: "2", "Progressive", "点进式", "2번"
    > ---------------------------------------------------------------------------------

3. **WAIT**: Do NOT generate any code until user replies.
4. **CREATE**: After reply, create `PROJECT_STATUS.md` with:
    - `Governance Mode`: [User Selection]
    - `Project Skeleton`: [Tree View]
    - `Tech Stack`: [Detected Stack]
    - `Architectural Decisions`: []
    - `Technical Debt`: []
    - `Design Audit Status`: []

### `READ_STATUS` (Regular Start)

1. **ACTION**: Read `PROJECT_STATUS.md`.
2. **CHECK**: Value of `Governance Mode`.
    - `Refactor` -> Enforce strict directory rules.
    - `Progressive` -> Allow old structure, enforce new code quality.
    - `Legacy` -> Mimic existing style.

## 🗂️ Project Governance Layer (Project-Level Workflow Rules)

**Instruction for AI Agents:**  
If a file named `PROJECT_GOVERNANCE.md` exists in the project root, you MUST treat it as the active project-level governance specification.

### 📌 Priority & Precedence

1. **Protocol Layer Always Overrides**  
   Rules defined inside `.agents/` and this `AGENTS.md` are **higher priority** and CANNOT be overwritten by project governance.

2. **Project Governance Overrides Workflow Behavior**  
   The following behaviors MUST follow `PROJECT_GOVERNANCE.md`:
   - Development workflow steps (planning → implementation → testing → documentation)
   - File structure conventions
   - Commit message style
   - Testing requirements
   - Documentation update behavior

3. **Governance Autoload**  
   Upon every turn, after loading `.agents/*` rules, AI MUST load and obey: `PROJECT_GOVERNANCE.md` (if present).

<!-- FINAL REMINDER -->
> [!IMPORTANT]
> **PASSIVE MEMORY ENFORCEMENT**: Before executing ANY task, verify your plan against `context/memory.md`.
> Core Memory Path: `context/memory.md`
