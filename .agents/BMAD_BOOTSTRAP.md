# BMAD Method Bootstrap Instruction (v7.5 Ultimate)

This file ensures that the BMAD (Behavior-Modulated Automatic Development) method is automatically available.

You — the LLM running inside the IDE — should obey this file *immediately on project load*.

---

## 1. Dynamic Environment Detection

Perform detection to identify the active BMAD runtime:

1. **Scan**: Check for `bmad/` or `_bmad/`.
2. **Identify**:
   - IF folder has `bmad.fingerprint.json` OR contains `core/` and `bmm/` -> **Active Runtime**.
   - IF folder exists but **is empty or missing core structure** -> **User Conflict Folder**.

**States to store in memory**:

```text
ACTIVE_BMAD_PATH = "bmad/" OR "_bmad/" OR null
BMAD_CONFLICT_PATH = path-to-user-folder OR null
```

---

## 2. Smart Installation Strategy (Non-Intrusive)

If `ACTIVE_BMAD_PATH` is null, execute the following logic.

### ⛔ Pre-Installation Check (MANDATORY)

Before attempting installation, you **MUST** verify the Node.js environment.

1. **Check**: Run `node -v` (and check for >= v20).
2. **Decision**:
   - [PASS] -> Proceed to Scenario A or B.
   - [FAIL] -> **STOP IMMEDIATELY**. Do not attempt installation. Display the following:

   > **⚠️ BMAD Installation Skipped / BMAD 安装已跳过**
   >
   > **Reason**: Node.js (v20+) is required but not detected.
   > **原因**：未检测到 Node.js (v20+) 环境。
   >
   > **Action**: Falling back to Standard Mode.
   > **操作**：自动降级为标准模式。

---

### Scenario A: No Conflict

1. Execute: `pwsh -Command "Write-Output '', 'y' | npx -y bmad-method install"` (Windows) or `printf '\ny\n' | npx -y bmad-method install` (Linux/Mac).
2. Set `ACTIVE_BMAD_PATH = "bmad/"`

### Scenario B: Conflict Detected (`BMAD_CONFLICT_PATH` == "bmad/")

**Goal**: Install BMAD into `_bmad/` while keeping user's `bmad/` folder untouched.

**Procedure (CLI Execution)**:

1. **Swap (Temporary Move)**:
   - Windows: `ren bmad bmad_temp_hold`
   - Linux/Mac: `mv bmad bmad_temp_hold`

2. **Install**:
   - Execute: `pwsh -Command "Write-Output '', 'y' | npx -y bmad-method install"` (Windows) or `printf '\ny\n' | npx -y bmad-method install` (Linux/Mac).
   - (This creates a new `bmad/` folder with the runtime).

3. **Shift**:
   - Rename the **new** `bmad/` to `_bmad/`.
   - Windows: `ren bmad _bmad`
   - Linux/Mac: `mv bmad _bmad`

4. **Restore**:
   - Move the user's folder back to original name.
   - Windows: `ren bmad_temp_hold bmad`
   - Linux/Mac: `mv bmad_temp_hold bmad`

5. **Finalize**:
   - Set `ACTIVE_BMAD_PATH = "_bmad/"`

> [!WARNING]
> **Failure Recovery**: If any step (2-4) fails mid-way, you MUST restore the user's original folder:
> - Windows: `if exist bmad_temp_hold (ren bmad_temp_hold bmad)`
> - Linux/Mac: `[ -d bmad_temp_hold ] && mv bmad_temp_hold bmad`
> 
> Always verify `bmad_temp_hold` does not remain after completion.

---

## 3. Persistent Load Strategy

After detection/installation:

1. **Relative Pathing**: Load all configurations using the relative `ACTIVE_BMAD_PATH`.
2. **Graceful Fallback**: If installation fails, proceed in Standard Mode.

---

## 4. Multi-Platform CLI Interaction Rules

| Action | Windows (cmd/pwsh) | Linux/macOS (sh/bash) |
| :--- | :--- | :--- |
| **Detect** | `dir /ad /b` | `ls -d */` |
| **Rename** | `ren <old> <new>` | `mv <old> <new>` |

---

## 5. Summary for the IDE LLM

- **User First**: NEVER permanently rename or delete a user-created `bmad/` folder.
- **Smart Namespace**: Use `_bmad/` if the default name is taken.
- **Atomic Logic**: Ensure the "Swap-Install-Restore" sequence is completed atomically to restore user paths.

This file is the single point of truth for dynamic bootstrap logic.
