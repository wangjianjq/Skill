#!/usr/bin/env bash
# AI Agent Lint - Bash Script
# 用于检查 AI Agent 项目的代码质量

set -eo pipefail

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
GRAY='\033[0;90m'
NC='\033[0m' # No Color

# 参数解析
PATH_TARGET="${1:-.}"
FIX_MODE=false
VERBOSE=false

for arg in "$@"; do
    case $arg in
        --fix) FIX_MODE=true ;;
        --verbose) VERBOSE=true ;;
    esac
done

echo -e "${CYAN}🔍 AI Agent Lint - 正在检查项目...${NC}"
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ 错误: 未检测到 Python${NC}"
    echo ""
    echo -e "${YELLOW}📥 请安装 Python 3.10 或更高版本:${NC}"
    echo -e "${YELLOW}   https://www.python.org/downloads/${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo -e "${GREEN}✅ Python: $PYTHON_VERSION${NC}"

# 检查 Ruff
if ! command -v ruff &> /dev/null; then
    echo -e "${YELLOW}⚠️  警告: 未检测到 Ruff${NC}"
    echo ""
    echo -e "${CYAN}📥 正在尝试安装 Ruff...${NC}"
    
    if pip install ruff --quiet 2>/dev/null; then
        echo -e "${GREEN}✅ Ruff 安装成功!${NC}"
    else
        echo -e "${RED}❌ 自动安装失败，请手动安装:${NC}"
        echo -e "${YELLOW}   pip install ruff${NC}"
        echo ""
        echo -e "${CYAN}💡 或使用 pipx 安装全局版本:${NC}"
        echo -e "${CYAN}   pipx install ruff${NC}"
        exit 1
    fi
fi

RUFF_VERSION=$(ruff --version)
echo -e "${GREEN}✅ Ruff: $RUFF_VERSION${NC}"

echo ""
echo -e "${GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# 解析目标路径
if [ ! -d "$PATH_TARGET" ]; then
    echo -e "${RED}❌ 错误: 路径不存在: $PATH_TARGET${NC}"
    exit 1
fi

PATH_ABSOLUTE=$(cd "$PATH_TARGET" && pwd)
echo -e "${CYAN}📁 扫描目录: $PATH_ABSOLUTE${NC}"

# 检测项目类型
PROJECT_TYPE="通用 Python 项目"
if ls "$PATH_ABSOLUTE"/*langchain* 1> /dev/null 2>&1; then
    PROJECT_TYPE="LangChain 项目"
elif ls "$PATH_ABSOLUTE"/*autogen* 1> /dev/null 2>&1; then
    PROJECT_TYPE="AutoGen 项目"
elif ls "$PATH_ABSOLUTE"/*crewai* 1> /dev/null 2>&1; then
    PROJECT_TYPE="CrewAI 项目"
fi

echo -e "${CYAN}📦 项目类型: $PROJECT_TYPE${NC}"
echo ""

# 构建 Ruff 命令
RUFF_CMD="ruff check \"$PATH_ABSOLUTE\""

if [ "$FIX_MODE" = true ]; then
    RUFF_CMD="$RUFF_CMD --fix"
    echo -e "${YELLOW}🔧 自动修复模式: 已启用${NC}"
    echo ""
fi

if [ "$VERBOSE" = true ]; then
    RUFF_CMD="$RUFF_CMD --verbose"
fi

# 执行检查
echo -e "${GREEN}🚀 开始检查...${NC}"
echo ""

eval $RUFF_CMD
EXIT_CODE=$?

echo ""
echo -e "${GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# 输出结果
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✅ 检查完成: 未发现问题!${NC}"
else
    echo -e "${YELLOW}⚠️  检查完成: 发现问题，请查看上方详情${NC}"
    echo ""
    if [ "$FIX_MODE" = false ]; then
        echo -e "${CYAN}💡 提示: 使用 --fix 参数可自动修复部分问题${NC}"
        echo -e "${GRAY}   示例: ./lint.sh . --fix${NC}"
    fi
fi

echo ""
exit $EXIT_CODE
