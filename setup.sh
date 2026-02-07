#!/bin/bash

echo "[AGENTS-MD] Bootstrapping Environment..."

# Check for uv
if ! command -v uv &> /dev/null; then
    echo "[AGENTS-MD] 'uv' not found. Installing..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to install uv. Please install manually."
        exit 1
    fi
    
    # Source the env to get uv in path immediately if possible, 
    # though usually requires shell restart or sourcing .cargo/env
    if [ -f "$HOME/.cargo/env" ]; then
        source "$HOME/.cargo/env"
    fi
fi

# Check for Node.js
if ! command -v node &> /dev/null && ! command -v nodejs &> /dev/null; then
    echo "[WARNING] Node.js not found. BMad-Method will run in degraded mode."
    echo "          Install Node.js v20+ for full functionality."
fi



touch .ag_env_verified
echo "[AGENTS-MD] Setup Complete. Agent Environment is ready for Passive Context."
