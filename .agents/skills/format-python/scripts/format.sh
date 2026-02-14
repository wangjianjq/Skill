#!/usr/bin/env bash
# Python Format - Bash Script

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
CHECK_MODE=false
VERBOSE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --check) CHECK_MODE=true; shift ;;
        --verbose) VERBOSE=true; shift ;;
        *) PATH_TARGET="$1"; shift ;;
    esac
done

echo -e "${CYAN}🎨 Python Format - 正在格式化代码...${NC}"
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

# 检查 Black
if ! command -v black &> /dev/null; then
    echo -e "${YELLOW}⚠️  警告: 未检测到 Black${NC}"
    echo ""
    echo -e "${CYAN}📥 正在尝试安装 Black...${NC}"
    
    if pip install black --quiet 2>/dev/null || pip3 install black --quiet 2>/dev/null; then
        echo -e "${GREEN}✅ Black 安装成功!${NC}"
        BLACK_VERSION=$(black --version)
        echo -e "   ${GREEN}版本: $BLACK_VERSION${NC}"
    else
        echo -e "${RED}❌ 自动安装失败，请手动安装:${NC}"
        echo -e "${YELLOW}   pip install black${NC}"
        echo ""
        echo -e "${CYAN}💡 或使用 pipx 安装全局版本（推荐）:${NC}"
        echo -e "${CYAN}   pipx install black${NC}"
        exit 1
    fi
else
    BLACK_VERSION=$(black --version)
    echo -e "${GREEN}✅ Black: $BLACK_VERSION${NC}"
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
BLACK_ARGS=("$PATH_ABSOLUTE")

if [ "$CHECK_MODE" = true ]; then
    BLACK_ARGS+=("--check")
    echo -e "${YELLOW}🔍 检查模式: 仅检查不修改${NC}"
    echo ""
fi

if [ "$VERBOSE" = true ]; then
    BLACK_ARGS+=("--verbose")
fi

# 执行格式化
echo -e "${GREEN}🚀 开始执行...${NC}"
echo ""

black "${BLACK_ARGS[@]}"
EXIT_CODE=$?

echo ""
echo -e "${GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# 输出结果
if [ $EXIT_CODE -eq 0 ]; then
    if [ "$CHECK_MODE" = true ]; then
        echo -e "${GREEN}✅ 格式检查通过: 未发现问题!${NC}"
    else
        echo -e "${GREEN}✅ 格式化完成!${NC}"
    fi
else
    if [ "$CHECK_MODE" = true ]; then
        echo -e "${YELLOW}⚠️  格式检查失败: 发现代码风格问题${NC}"
        echo -e "${GRAY}   请运行不带 --check 参数的命令以自动修复${NC}"
    else
        echo -e "${RED}❌ 格式化过程中出现错误${NC}"
    fi
fi

echo ""
exit $EXIT_CODE
