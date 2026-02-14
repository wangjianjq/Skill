#!/bin/bash

# Ensure we run from the project root (where this script lives)
cd "$(dirname "$0")"

echo "[AGENTS-MD] Bootstrapping Environment..."

# Check for uv
if ! command -v uv &> /dev/null; then
    echo "[AGENTS-MD] 'uv' not found. Installing..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to install uv. Please install manually."
        exit 1
    fi
    
    # Source the env to get uv in path immediately
    if [ -f "$HOME/.local/bin/uv" ]; then
        export PATH="$HOME/.local/bin:$PATH"
    elif [ -f "$HOME/.cargo/env" ]; then
        source "$HOME/.cargo/env"
    fi
fi

# Check for Node.js
if ! command -v node &> /dev/null && ! command -v nodejs &> /dev/null; then
    echo "[WARNING] Node.js not found. BMad-Method will run in degraded mode."
    echo "          Install Node.js v20+ for full functionality."
fi

# Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "[AGENTS-MD] Installing dependencies from requirements.txt..."
    if command -v uv &> /dev/null; then
        uv pip install -r requirements.txt
    else
        pip install -r requirements.txt
    fi
fi



touch .ag_env_verified

# Function to create PROJECT_STATUS.md (must be defined before use)
create_status() {
    local mode=$1
    local current_date=$(date +%Y-%m-%d)
    
    cat <<EOF > PROJECT_STATUS.md
# PROJECT_STATUS.md

## Schema: Project Status

- document_type: project_status_tracking
- governance_mode: $mode
- target_audience: ai_agents
- enforcement_level: mandatory
- last_updated: $current_date
- compatible_with: Agents-MD Pro v8.0

---

## Governance Mode / 治理模式

**Mode**: $mode ✅

**Description**: 
$(if [ "$mode" == "Progressive" ]; then echo "Keep old files, write new code via protocol. / 保留旧文件，新代码遵循协议规范。"; 
  elif [ "$mode" == "Frozen" ]; then echo "Strict version control, no upgrades. / 严格保持现有依赖版本，不做任何升级。"; 
  else echo "Proactive modernization and refactoring. / 主动提议现代化重构和依赖升级。"; fi)

---

## Project Skeleton / 项目结构

\`\`\`
Skill/
├── .agents/             # Protocol Land (Immutable Core Rules)
├── scripts/             # Core Utilities & Configuration
├── bmad/             # BMAD Method workflows
├── context/          # Memory and status
├── docs/                # Documentation
├── AGENTS_INDEX.yaml    # Knowledge Index
├── *.md                 # Master boot and AI adapters
├── *.py              # Utility scripts
└── setup.bat/sh      # Environment setup
\`\`\`

---

## Tech Stack / 技术栈

- **Languages**: Python (utility scripts)
- **Protocols**: Agents-MD Pro v8.0, BMAD Method
- **Supported Languages**: zh-CN, en

---

## Architectural Decisions / 架构决策

| ADR | Title | Status |
|-----|-------|--------|
| ADR-001 | 混合智能架构 | ✅ Active |
| ADR-002 | 禁用 Eval | ✅ Active |
| ADR-003 | 认知镜像协议 | ✅ Active |

---

## Technical Debt / 技术债务

- [ ] None recorded yet

---

## Design Audit Status / 设计审计状态

- **Status**: Not Started
- **Last Audit**: N/A

---

## LastTask / 最近任务

| Field | Value |
|-------|-------|
| Task | Project Initialization |
| Status | ✅ Completed |
| Date | $current_date |

---

## Changelog / 变更日志

### $current_date
- chore: Project initialized with $mode mode via setup script.
EOF
    
    echo "[OK] PROJECT_STATUS.md created with $mode mode"
}

# Check for PROJECT_STATUS.md
if [ ! -f "PROJECT_STATUS.md" ]; then
    echo ""
    echo "========================================================"
    echo "[AGENTS-MD] First-time setup detected."
    echo "========================================================"
    echo ""
    echo "Please select a Governance Mode:"
    echo ""
    echo "  [1] Frozen      - Strict version control, no upgrades"
    echo "  [2] Progressive - Balance stability and innovation (Recommended)"
    echo "  [3] Aggressive  - Proactive modernization"
    echo ""
    read -p "Enter your choice (1/2/3) [Default: 2]: " mode
    
    # Default to 2 if empty
    mode=${mode:-2}
    
    case $mode in
        1)
            echo ""
            echo "[AGENTS-MD] Creating PROJECT_STATUS.md with Frozen mode..."
            create_status "Frozen"
            ;;
        2)
            echo ""
            echo "[AGENTS-MD] Creating PROJECT_STATUS.md with Progressive mode..."
            create_status "Progressive"
            ;;
        3)
            echo ""
            echo "[AGENTS-MD] Creating PROJECT_STATUS.md with Aggressive mode..."
            create_status "Aggressive"
            ;;
        *)
            echo ""
            echo "[WARNING] Invalid choice. Defaulting to Progressive mode..."
            create_status "Progressive"
            ;;
    esac
    echo ""
fi

echo "[AGENTS-MD] Setup Complete. Agent Environment is ready for Passive Context."

