# PROJECT_GOVERNANCE.md

## Schema: Governance Configuration

- document_type: project_governance_specification
- governance_type: project_workflow
- target_audience: ai_agents
- enforcement_level: mandatory
- language_policy: bilingual (zh-CN + en)
- compatible_with: Agents-MD Pro v7.5
- last_updated: 2026-02-03
- workflow_stages: 5 (scope → design → implementation → testing → documentation)

---

Project-Level Governance Specification  
Compatible with Agents-MD Pro v7.5 Passive Context System

---

# 1. Development Workflow (Lightweight Team Model)

All tasks MUST follow this flow:

## Step 1 — Scope Confirmation

AI must:

- Ask the user to confirm task scope
- Record summary in `PROJECT_STATUS.md` → section `LastTask`

## Step 2 — Mini Design (3–7 lines)

Before writing code, AI MUST produce a short design.

### 🌐 Language Requirement (Mandatory)

- **User Language First**: The plan/design MUST be generated in the **User's Native Language** (e.g., Chinese for CN users).
- **Bilingual Option**: Bilingual (User Language + English) is highly encouraged.
- **English-Only Exception**: Only acceptable if the user's primary language IS English.

### Content Checklist

- Target behavior
- Affected files
- Function signatures
- Edge cases / risks

Coding MUST halt until user approves.

## Step 3 — Implementation

AI must:

- Follow `.agents/` language/framework rules
- Follow confirmed design
- Modify only allowed paths (User Land)
- Never touch `.agents/`, `.agent/`, or `bmad/`
- **Template Compliance**: When creating new protocol files, MUST use standard templates:
  - `.agents/templates/LANG_TEMPLATE.md` for language specs
  - `.agents/templates/SKILL_TEMPLATE.md` for skill protocols
  - `.agents/templates/FW_TEMPLATE.md` for framework specs
  - All new protocol files MUST include `## Schema:` metadata block
  - *(Optional: `.agents/templates/GUIDE.md` has supplementary examples if needed)*

## Step 4 — Self-Testing

AI must:

- Validate logic consistency
- Ensure imports/paths/naming are correct
- Create/update minimal test cases under `/tests`
- Warn the user if tests are skipped

## Step 5 — Documentation Update

AI MUST update:

- `CHANGELOG.md` (required)
- Any related design md (if exists, optional)
- Must not write useless or redundant documentation

---

# 2. CHANGELOG Policy (Must-Follow Rule)

File location:

## CHANGELOG Dual-Language Policy（双语变更日志规则）

为了确保 AI IDE 在自动维护 CHANGELOG.md 时能够保持一致性、专业性和可读性，
所有变更记录必须同时包含中文与英文描述。
To ensure consistency, professionalism, and readability when the AI IDE automatically maintains
CHANGELOG.md, every change entry must include both Chinese and English descriptions.

---

### 记录格式要求（Entry Format Requirements）

每条变更记录必须遵循以下格式：
Each entry must follow this structure:

- {type}: {中文描述} / {English description}

其中 type 必须为以下之一：
Where `type` must be one of the following:

- feat: 新功能 / New feature  
- fix: 问题修复 / Bug fix  
- refactor: 重构或结构性变更 / Code or structure refactor  
- chore: 文档、依赖、脚本或工程维护 / Documentation or maintenance  

中文描述需准确表达变更内容；
Chinese description should accurately reflect what changed.  
英文描述应为简明、专业的软件工程术语，与中文语义完全一致；
English description must be concise and technical, strictly matching the meaning of the Chinese text.

---

### 生成规则（Generation Rules）

1. AI 必须在每次任务完成后追加新的 CHANGELOG 条目。  
   The AI must append a new changelog entry after every completed task.

2. 每个日期分组使用二级标题格式：  
   Every date block must use a level-2 heading with format `## YYYY-MM-DD`.

3. 新条目追加于对应日期分组的最后一行（不覆盖已有条目）。  
   New entries are appended to the end of the date block (never overwrite existing entries).

4. 禁止生成重复、冗余或无意义的条目。  
   Redundant, duplicate, or trivial entries are FORBIDDEN.

---

### 自动维护规则（Automatic Maintenance Rules）

AI 在自动维护 CHANGELOG 时必须遵守以下规则：
The AI must follow these rules when auto-maintaining CHANGELOG:

1. 仅在任务实际完成后追加条目，不得预写或推测未完成的工作。  
   Only append entries AFTER task completion. Never pre-write or speculate.

2. 每条变更必须与实际代码修改一一对应。  
   Each entry must correspond to actual code changes.

3. 如当日无变更，不得创建空的日期分组。  
   Do not create empty date blocks if no changes occurred.

---

# 3. Report Language Policy (报告语言策略)

## Mandatory Chinese Reporting / 强制中文报告

**Rule**: All summaries, audit reports, and conversational updates provided by the AI MUST be in Chinese.
**规则**: AI 提供的所有摘要、审计报告和对话更新必须使用中文。

- **Reason**: User preference and project standard.
- **Exceptions**: Technical terms, code snippets, or direct quotes from English docs.
- **Override**: This rule is **subordinate** to AGENTS.md § "Cognitive Mirroring Protocol". If the user communicates in a language other than Chinese, that language takes precedence per AGENTS.md §0.
- **覆盖说明**: 此规则**从属于** AGENTS.md § "认知镜像协议"。如用户以非中文交流，以用户语言为准。

---

# 4. README Synchronization Management（README 同步管理）

## 背景（Background）

README 文件是面向人类开发者和 GitHub 访客的文档，而 AGENTS.md 和 AGENTS_INDEX.yaml 是 AI 的操作协议。  
README files are human-facing documentation for developers and GitHub visitors, while AGENTS.md and AGENTS_INDEX.yaml are AI operating protocols.

为了避免信息漂移，AI 在日常开发中严格禁止读取 README。  
To prevent information drift, AI is strictly forbidden from reading README during regular development.

---

## 同步触发机制（Sync Trigger Mechanism）

AI 仅在以下**显式触发**条件下执行 README 同步：  
AI performs README sync ONLY under these **explicit triggers**:

### 触发短语（Trigger Phrases）

用户必须使用以下任一短语：  
User must use one of these exact phrases:

- **EN**: `sync README`, `update README`, `refresh README`
- **ZH**: `同步 README`, `更新 README`, `刷新 README`

### 禁止行为（Forbidden Behaviors）

AI **严禁**以下行为：  
AI is **STRICTLY FORBIDDEN** from:

1. 主动建议 README 同步（除非检测到明显的用户困惑）  
   Proactively suggesting README sync (unless detecting obvious user confusion)

2. 在完成功能开发后自动同步 README  
   Auto-syncing README after feature completion

3. 基于 README 内容做出技术决策  
   Making technical decisions based on README content

---

## 同步协议（Sync Protocol）

### 步骤序列（Step Sequence）

AI 必须严格按照以下步骤执行：  
AI must strictly follow this sequence:

**Step 1**: 确认同步意图 / Confirm sync intent

```
"README Sync Mode Activated / README 同步模式已激活

This will read current README files and synchronize them with AGENTS_INDEX.yaml.
本操作将读取当前 README 文件并与 AGENTS_INDEX.yaml 同步。

Source of Truth: AGENTS_INDEX.yaml → README
信息源头：AGENTS_INDEX.yaml → README

Proceed? / 继续？"
```

**Step 2**: 读取权威数据源 / Read authoritative source

- Load `AGENTS_INDEX.yaml` (contains all supported technologies)
- Load `AGENTS.md` knowledge index (compressed format)

**Step 3**: 例外读取 README / Exception read of README

- Read `README.md` (Primary GitHub-rendered document / GitHub 主显示文档)
- Read `README.txt` (English plain-text version)
- Read `README_zh-CN.txt` (Chinese plain-text version)
- **Critical**: This is the ONLY permitted README read

**Step 4**: 生成差异报告 / Generate diff report

Report must include:

- ✅ New capabilities in AGENTS_INDEX.yaml not listed in README
- ⚠️ Outdated technology versions in README
- ❌ Technologies listed in README but removed from protocols
- 📊 Statistics: Total protocols in AGENTS_INDEX.yaml vs README

**Step 5**: 请求用户批准 / Request user approval

Present changes in bilingual format:

```
## Proposed Changes / 建议变更

### New Additions / 新增内容
1. [EN] HarmonyOS support (ArkTS, ArkUI)
   [ZH] 鸿蒙系统支持（ArkTS、ArkUI）

### Updates / 更新内容
1. [EN] Flutter: 3.10+ → 3.24+
   [ZH] Flutter 版本：3.10+ → 3.24+

Approve all changes? (Y/N) / 批准所有变更？（是/否）
```

**Step 6**: 执行更新 / Execute updates

- Update both README files simultaneously
- Maintain existing README structure and style
- Update "Last Audited" date to current date (YYYY-MM-DD format)

**Step 7**: 记录变更日志 / Record in CHANGELOG

```
- docs: 同步 README 至 AGENTS_INDEX.yaml 最新状态 / Synced README to match latest AGENTS_INDEX.yaml
```

**Step 8**: **内存清除** / **Memory purge**

- Treat README content as sensitive data
- Immediately purge from working memory
- Next task MUST NOT reference README content

---

## 双语同步规则（Bilingual Sync Rules）

### 强制要求（Mandatory Requirements）

1. **同步所有 README 文件**：`README.md`、`README.txt` 和 `README_zh-CN.txt` 必须同时更新  
   **Sync all README files**: `README.md`, `README.txt`, and `README_zh-CN.txt` must be updated together

2. **语义一致**：中英文描述必须语义完全一致  
   **Semantic consistency**: Chinese and English descriptions must match exactly

3. **版本日期**：两个文件的 "Last Audited" 日期必须相同  
   **Audit date**: Both files must have identical "Last Audited" dates

### 质量门控（Quality Gates）

更新后的 README 必须满足：  
Updated README must satisfy:

- ✅ All technologies in AGENTS_INDEX.yaml are listed
- ✅ No outdated version numbers
- ✅ No technologies absent from AGENTS_INDEX.yaml
- ✅ Bilingual consistency verified
- ✅ Markdown formatting valid (no lint errors)

---

## 冲突解决（Conflict Resolution）

### 优先级规则（Precedence Rules）

当 README 与协议冲突时：  
When README conflicts with protocols:

| 信息源 | 优先级 | 处理方式 |
|:------|:------|:--------|
| **AGENTS_INDEX.yaml** | 🥇 Highest | Always correct, README must follow |
| **AGENTS.md** | 🥈 High | Defines AI behavior, overrides README |
| **README.txt** | 🥉 Low | Human reference, must sync to match protocols |

### 错误处理（Error Handling）

**场景 1**: 用户报告 "README 说支持 X，但 AI 不知道"  
**Scenario 1**: User reports "README says X is supported, but AI doesn't know"

- **诊断** / **Diagnosis**: README 可能手动编辑但未同步到协议  
  README may have been manually edited without syncing to protocols
- **解决** / **Solution**: 执行 README 同步，以 AGENTS_INDEX.yaml 为准  
  Execute README sync, using AGENTS_INDEX.yaml as source of truth

**场景 2**: 用户问 "为什么 README 里没有 Y?"  
**Scenario 2**: User asks "Why is Y not in README?"

- **诊断** / **Diagnosis**: 协议已添加 Y，但 README 未同步  
  Protocol added Y, but README not synced
- **解决** / **Solution**: 建议用户触发 README 同步  
  Suggest user trigger README sync

---

## CHANGELOG 与 README 的关系（CHANGELOG-README Relationship）

### 记录规则（Recording Rules）

当 CHANGELOG 中出现 "README" 相关条目时：  
When CHANGELOG contains README-related entries:

1. **同步操作**：必须记录为 `docs: 同步 README...`  
   **Sync operations**: Must record as `docs: Synced README...`

2. **手动编辑**：如果用户手动修改 README，AI 不记录（因为 AI 不读取）  
   **Manual edits**: If user manually edits README, AI does not record (because AI doesn't read it)

3. **验证责任**：README 变更的准确性由**人类开发者**验证  
   **Verification responsibility**: README change accuracy verified by **human developers**

### AI 记录限制（AI Recording Limitations）

AI 在 CHANGELOG 中记录 README 变更时：  
When AI records README changes in CHANGELOG:

- ✅ **可以**：记录同步操作本身（"已执行 README 同步"）  
  **CAN**: Record sync operation itself ("README sync executed")
- ❌ **不可以**：列举 README 具体内容变更（AI 不应保留 README 细节）  
  **CANNOT**: List specific README content changes (AI should not retain README details)

**正确示例** / **Correct example**:

```
- docs: 同步 README 至 AGENTS_INDEX.yaml (新增鸿蒙支持) / Synced README to AGENTS_INDEX.yaml (added HarmonyOS support)
```

**错误示例** / **Wrong example**:

```
- docs: 更新 README 第 42 行描述 / Updated README line 42 description
       ❌ Too specific, implies AI retained README content
```

---

## 审计周期建议（Audit Cycle Recommendation）

建议的 README 同步周期：  
Recommended README sync frequency:

| 触发条件 | 建议周期 | 原因 |
|:--------|:--------|:-----|
| 新增主要协议（语言/框架） | **立即** | 影响项目宣传的核心能力 |
| 版本号更新 | **月度** | 保持技术栈信息新鲜 |
| 项目结构调整 | **按需** | 结构变化较少发生 |
| 日常功能开发 | **不需要** | README 不反映具体功能细节 |

Major protocol additions (languages/frameworks): **Immediate**  
Version updates: **Monthly**  
Structure changes: **As needed**  
Regular feature development: **Not required**
