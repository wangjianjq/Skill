#!/usr/bin/env bash
# Docker Lint - Bash Script

set -eo pipefail

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
GRAY='\033[0;90m'
NC='\033[0m'

# 参数解析
FILE_TARGET="Dockerfile"
PATH_TARGET="."
RECURSIVE=false
CONFIG_FILE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -r|--recursive) RECURSIVE=true; shift ;;
        -c|--config) CONFIG_FILE="$2"; shift 2 ;;
        *) 
            if [ -z "$FILE_SET" ]; then
                FILE_TARGET="$1"
                FILE_SET=true
            fi
            shift
            ;;
    esac
done

echo -e "${CYAN}🐳 Docker Lint - 正在检查 Dockerfile...${NC}"
echo ""

# 检查 hadolint
HADOLINT_INSTALLED=false
USE_DOCKER=false

if command -v hadolint &> /dev/null; then
    HADOLINT_INSTALLED=true
    HADOLINT_VERSION=$(hadolint --version | head -n1)
    echo -e "${GREEN}✅ hadolint: $HADOLINT_VERSION${NC}"
else
    echo -e "${YELLOW}⚠️  警告: hadolint 未安装在系统路径${NC}"
    
    if command -v docker &> /dev/null; then
        echo -e "${GREEN}✅ Docker 可用，将使用容器运行 hadolint${NC}"
        USE_DOCKER=true
    else
        echo -e "${RED}❌ Docker 也不可用${NC}"
        echo ""
        echo -e "${YELLOW}📥 请安装 hadolint 或 Docker:${NC}"
        echo -e "${CYAN}   方法1: brew install hadolint (macOS)${NC}"
        echo -e "${CYAN}   方法2: wget -O /usr/local/bin/hadolint ...${NC}"
        echo -e "${CYAN}   方法3: 安装 Docker${NC}"
        exit 1
    fi
fi

echo ""
echo -e "${GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# 收集文件
DOCKERFILES=()

if [ "$RECURSIVE" = true ]; then
    while IFS= read -r -d '' file; do
        DOCKERFILES+=("$file")
    done < <(find "$PATH_TARGET" -type f -name "*Dockerfile*" -print0)
elif [ -f "$FILE_TARGET" ]; then
    DOCKERFILES+=("$FILE_TARGET")
else
    echo -e "${RED}❌ 错误: 找不到文件: $FILE_TARGET${NC}"
    exit 1
fi

if [ ${#DOCKERFILES[@]} -eq 0 ]; then
    echo -e "${RED}❌ 错误: 未找到任何 Dockerfile${NC}"
    exit 1
fi

echo -e "${CYAN}📁 找到 ${#DOCKERFILES[@]} 个 Dockerfile${NC}"
echo ""

TOTAL_ERRORS=0
TOTAL_WARNINGS=0

for dockerfile in "${DOCKERFILES[@]}"; do
    echo -e "${GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}📄 文件: $dockerfile${NC}"
    echo -e "${GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    # 执行检查
    if [ "$USE_DOCKER" = true ]; then
        DOCKERFILE_DIR=$(dirname "$dockerfile")
        DOCKERFILE_NAME=$(basename "$dockerfile")
        
        if [ -n "$CONFIG_FILE" ]; then
            CONFIG_DIR=$(dirname "$CONFIG_FILE")
            CONFIG_NAME=$(basename "$CONFIG_FILE")
            RESULT=$(docker run --rm -i \
                -v "${DOCKERFILE_DIR}:/workspace" \
                -v "${CONFIG_DIR}:/config" \
                hadolint/hadolint \
                --config "/config/$CONFIG_NAME" \
                < "/workspace/$DOCKERFILE_NAME" 2>&1) || true
        else
            RESULT=$(docker run --rm -i \
                -v "${DOCKERFILE_DIR}:/workspace" \
                hadolint/hadolint \
                < "/workspace/$DOCKERFILE_NAME" 2>&1) || true
        fi
    else
        ARGS=("$dockerfile")
        if [ -n "$CONFIG_FILE" ]; then
            ARGS+=(--config "$CONFIG_FILE")
        fi
        RESULT=$(hadolint "${ARGS[@]}" 2>&1) || true
    fi
    
    if [ -n "$RESULT" ]; then
        echo "$RESULT"
        ERRORS=$(echo "$RESULT" | grep -c "error:" || true)
        WARNINGS=$(echo "$RESULT" | grep -c "warning:" || true)
        TOTAL_ERRORS=$((TOTAL_ERRORS + ERRORS))
        TOTAL_WARNINGS=$((TOTAL_WARNINGS + WARNINGS))
    else
        echo -e "${GREEN}✅ 未发现问题${NC}"
    fi
    
    echo ""
done

echo -e "${GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}📊 检查结果:${NC}"

if [ $TOTAL_ERRORS -gt 0 ]; then
    echo -e "   ${RED}❌ 错误: $TOTAL_ERRORS 个${NC}"
else
    echo -e "   ${GREEN}❌ 错误: $TOTAL_ERRORS 个${NC}"
fi

if [ $TOTAL_WARNINGS -gt 0 ]; then
    echo -e "   ${YELLOW}⚠️  警告: $TOTAL_WARNINGS 个${NC}"
else
    echo -e "   ${GREEN}⚠️  警告: $TOTAL_WARNINGS 个${NC}"
fi

echo -e "${GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

if [ $TOTAL_ERRORS -gt 0 ]; then
    echo ""
    echo -e "${CYAN}💡 建议查看 SKILL.md 中的 Dockerfile 修复示例${NC}"
    exit 1
elif [ $TOTAL_WARNINGS -gt 0 ]; then
    exit 0
else
    echo ""
    echo -e "${GREEN}✅ 所有检查通过!${NC}"
    exit 0
fi
