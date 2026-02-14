#!/usr/bin/env bash
# JavaScript Format - Bash Script
set -eo pipefail
PATH_TARGET="${1:-.}"
CHECK_MODE=false
EXTENSIONS="js,jsx,ts,tsx,json,css,md"
[[ "$2" == "--check" ]] && CHECK_MODE=true

echo "🎨 JavaScript Format - Prettier"
echo ""

command -v node &>/dev/null || { echo "❌ Node.js 未安装: https://nodejs.org"; exit 1; }
if ! command -v prettier &>/dev/null; then
    echo "⚠️  正在安装 Prettier..."
    npm install -g prettier || { echo "❌ 请手动安装: npm install -g prettier"; exit 1; }
fi

PATTERN="${EXTENSIONS//,/,}"
if [ "$CHECK_MODE" = true ]; then
    prettier --check "$PATH_TARGET/**/*.{$PATTERN}"
else
    prettier --write "$PATH_TARGET/**/*.{$PATTERN}"
fi
exit $?
