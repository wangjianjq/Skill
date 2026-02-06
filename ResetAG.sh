#!/bin/bash
# [AGENTS-MD] Protocol Reset Tool (ResetAG)
# Purpose: Unlock the project and force re-initialization WITHOUT deleting the framework.

echo "========================================================"
echo "  AGENTS-MD PROTOCOL RESET TOOL (v7.5 Refined)"
echo "========================================================"
echo ""
echo "[!] WARNING: This will reset project-specific configurations."
echo "    Core framework directories (bmad, .agents) are preserved."
echo ""

# 1. Remove governance and status markers
echo "[1/3] Clearing state markers..."
# PROJECT_STATUS.md and USER_PROFILE.md are mandatory. Reset to clean templates.
# PROJECT_STATUS.md is mandatory. Initialize with clean template.
cat <<EOF > PROJECT_STATUS.md
# PROJECT_STATUS.md

## Governance Mode / 治理模式
Progressive / 渐进式

## Project Skeleton / 项目骨架
(To be populated by AI on first run / 待 AI 首次运行时填充)

## Tech Stack / 技术栈
[]

## Architectural Decisions / 架构决策
[]

## Technical Debt / 技术债务
[]

## Design Audit Status / 设计审计状态
[]

## Last Task / 上次任务
[None / 无]
EOF
echo "[OK] Initialized PROJECT_STATUS.md (Template)"

# USER_PROFILE.md is mandatory. Initialize with clean template.
cat <<EOF > USER_PROFILE.md
# USER_PROFILE.md

## User Preferences / 用户偏好

- **Communication Language / 沟通语言**: [Select: Chinese / English]
- **Role / 角色**: [Select: Developer / Architect / CTO]

## Persona Handshake / 角色握手

(To be populated during onboarding / 待入职期间填充)
EOF
echo "[OK] Initialized USER_PROFILE.md (Template)"
if [ -f "sprint-status.yaml" ]; then
    rm "sprint-status.yaml"
    echo "[OK] Removed sprint-status.yaml"
fi
if [ -f ".ag_env_verified" ]; then
    rm ".ag_env_verified"
    echo "[OK] Invalidated environment verification"
fi

# 2. Clear project-specific configurations
echo "[2/3] Resetting configurations..."
if [ -f "bmad/bmm/config.yaml" ]; then
    rm "bmad/bmm/config.yaml"
    echo "[OK] Reset BMAD BMM config"
fi
if [ -f "bmad/core/config.yaml" ]; then
    rm "bmad/core/config.yaml"
    echo "[OK] Reset BMAD Core config"
fi
if [ -d "_bmad-output" ]; then
    rm -rf "_bmad-output"
    echo "[OK] Cleaned up runtime output directory"
fi

# 3. Forced Context Logic
echo "[3/3] Forcing protocol re-indexing..."
if [ -f "AGENTS.md" ]; then
    touch "AGENTS.md"
    echo "[OK] Updated AGENTS.md timestamp"
fi

# 4. Distribution Mode (Optional)
echo ""
read -p "[?] Prepare for new distribution? (Reset CHANGELOG history) (y/N): " dist_mode
if [[ "$dist_mode" =~ ^[Yy]$ ]]; then
    echo "[4/4] Resetting CHANGELOG.md..."
    if [ -f "CHANGELOG.md" ]; then
        rm "CHANGELOG.md"
        echo "[OK] Deleted old CHANGELOG"
    fi
    cat <<EOF > CHANGELOG.md
# CHANGELOG

## Project Initialized

- chore: Project initialized for distribution.
EOF
    echo "[OK] Created fresh CHANGELOG.md"
fi


echo ""
echo "========================================================"
echo "[SUCCESS] Project state reset."
echo ""
echo "[ACTION REQUIRED] Please copy and paste the following to the AI:"
echo ""
echo "Protocol Reset. Read AGENTS.md to re-initialize."
echo "========================================================"
echo ""
