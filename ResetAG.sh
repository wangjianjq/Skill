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
if [ -f "PROJECT_STATUS.md" ]; then
    rm "PROJECT_STATUS.md"
    echo "[OK] Removed PROJECT_STATUS.md"
fi
if [ -f "sprint-status.yaml" ]; then
    rm "sprint-status.yaml"
    echo "[OK] Removed sprint-status.yaml"
fi
if [ -f "USER_PROFILE.md" ]; then
    rm "USER_PROFILE.md"
    echo "[OK] Removed USER_PROFILE.md"
fi
if [ -f ".ag_env_verified" ]; then
    rm ".ag_env_verified"
    echo "[OK] Invalidated environment verification"
fi
if [ -d ".git" ]; then
    echo ""
    echo "[WARNING] This will permanently delete the .git directory and all Git history!"
    read -p "Are you sure? (y/N): " confirm_git
    if [[ "$confirm_git" =~ ^[Yy]$ ]]; then
        rm -rf ".git"
        echo "[OK] Removed .git directory (for clean distribution)"
    else
        echo "[SKIP] .git directory preserved."
    fi
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
echo "[NEXT STEP] To re-initialize the project, run:"
echo "    ./setup.sh"
echo ""
echo "Or manually edit PROJECT_STATUS.md to set your governance mode."
echo ""
echo "[INFO] After initialization, you can start working with the AI."
echo "========================================================"
echo ""

