#!/usr/bin/env bash
# JavaScript Lint - Bash Script
set -eo pipefail
PATH_TARGET="${1:-.}"
FIX_MODE=false
EXTENSIONS="js,jsx,ts,tsx"
[[ "$2" == "--fix" ]] && FIX_MODE=true

echo "🔍 JavaScript Lint - ESLint"
echo ""

command -v node &>/dev/null || { echo "❌ Node.js 未安装: https://nodejs.org"; exit 1; }
if ! command -v eslint &>/dev/null; then
    echo "⚠️  正在安装 ESLint..."
    npm install -g eslint || { echo "❌ 请手动安装: npm install -g eslint"; exit 1; }
fi

ARGS=("$PATH_TARGET" --ext "$EXTENSIONS")
[ "$FIX_MODE" = true ] && ARGS+=(--fix)
eslint "${ARGS[@]}"
exit $?
