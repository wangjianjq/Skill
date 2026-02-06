#!/usr/bin/env bash
# Python Lint - Bash Script

set -eo pipefail

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
GRAY='\033[0;90m'
NC='\033[0m'

# 参数解析
PATH_TARGET="."
FIX_MODE=false
ERRORS_ONLY=false
VERBOSE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --fix) FIX_MODE=true; shift ;;
        --errors-only) ERRORS_ONLY=true; shift ;;
        --verbose) VERBOSE=true; shift ;;
        *) PATH_TARGET="$1"; shift ;;
    esac
done

echo -e "${CYAN}🐍 Python Lint - 正在检查代码...${NC}"
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo -e "${RED}❌ 错误: 未检测到 Python${NC}"
    echo ""
    echo -e "${YELLOW}📥 请安装 Python 3.8 或更高版本:${NC}"
    echo -e "${YELLOW}   https://www.python.org/downloads/${NC}"
    exit 1
fi

if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
else
    PYTHON_CMD=python
fi

PYTHON_VERSION=$($PYTHON_CMD --version)
echo -e "${GREEN}✅ Python: $PYTHON_VERSION${NC}"

# 检查 Ruff
if ! command -v ruff &> /dev/null; then
    echo -e "${YELLOW}⚠️  警告: 未检测到 Ruff${NC}"
    echo ""
    echo -e "${CYAN}📥 正在尝试安装 Ruff...${NC}"
    
    if pip install ruff --quiet 2>/dev/null || pip3 install ruff --quiet 2>/dev/null; then
        echo -e "${GREEN}✅ Ruff 安装成功!${NC}"
        RUFF_VERSION=$(ruff --version)
        echo -e "   ${GREEN}版本: $RUFF_VERSION${NC}"
    else
        echo -e "${RED}❌ 自动安装失败，请手动安装:${NC}"
        echo -e "${YELLOW}   pip install ruff${NC}"
        echo ""
        echo -e "${CYAN}💡 或使用 pipx 安装全局版本（推荐）:${NC}"
        echo -e "${CYAN}   pipx install ruff${NC}"
        exit 1
    fi
else
    RUFF_VERSION=$(ruff --version)
    echo -e "${GREEN}✅ Ruff: $RUFF_VERSION${NC}"
fi

echo ""
echo -e "${GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# 验证路径
if [ ! -d "$PATH_TARGET" ] && [ ! -f "$PATH_TARGET" ]; then
    echo -e "${RED}❌ 错误: 路径不存在: $PATH_TARGET${NC}"
    exit 1
fi

PATH_ABSOLUTE=$(cd "$(dirname "$PATH_TARGET")" && pwd)/$(basename "$PATH_TARGET")
echo -e "${CYAN}📁 扫描目录: $PATH_ABSOLUTE${NC}"
echo ""

# 构建命令
# 使用数组来安全地处理参数
RUFF_CMD=("ruff" "check" "$PATH_ABSOLUTE")

if [ "$FIX_MODE" = true ]; then
    RUFF_CMD+=("--fix")
    echo -e "${YELLOW}🔧 自动修复模式: 已启用${NC}"
    echo ""
fi

if [ "$ERRORS_ONLY" = true ]; then
    RUFF_CMD+=("--select" "E,F")
    echo -e "${YELLOW}⚠️  仅显示错误（忽略警告）${NC}"
    echo ""
fi

if [ "$VERBOSE" = true ]; then
    RUFF_CMD+=("--verbose")
fi

# 执行检查
echo -e "${GREEN}🚀 开始检查...${NC}"
echo ""

"${RUFF_CMD[@]}"
EXIT_CODE=$?

echo ""
echo -e "${GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# 输出结果
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✅ 检查完成: 未发现问题!${NC}"
else
    echo -e "${YELLOW}⚠️  检查完成: 发现问题，请查看上方详情${NC}"
    echo ""
    echo -e "${CYAN}💡 提示:${NC}"
    
    if [ "$FIX_MODE" = false ]; then
        echo -e "${GRAY}   - 使用 --fix 参数可自动修复部分问题${NC}"
        echo -e "${GRAY}     示例: ./lint.sh --fix${NC}"
    fi
    
    echo -e "${GRAY}   - 使用 --errors-only 仅显示错误${NC}"
    echo -e "${GRAY}     示例: ./lint.sh --errors-only${NC}"
fi

echo ""
exit $EXIT_CODE
