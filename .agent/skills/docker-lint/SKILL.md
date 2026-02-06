---
name: docker-lint
description: Dockerfile 最佳实践检查 - 使用 hadolint 验证 Dockerfile 安全性、性能和规范
---

# Docker Lint Skill

## 📋 概述

此 skill 使用 **hadolint**（Dockerfile linter）检查 Docker 镜像构建文件的最佳实践，确保：

- 🔒 安全性（非 root 用户、最小权限）
- ⚡ 性能优化（Layer 缓存、多阶段构建）
- 📏 规范遵循（Docker 官方最佳实践）
- 🐛 常见错误检测（拼写错误、无效指令）

## 🔧 前置条件 (Prerequisites)

| 工具 | 最低版本 | 检查命令 | 安装参考 |
|-----|---------|---------|---------|
| Docker | 20.10+ | `docker --version` | [docker.com](https://www.docker.com/) |
| hadolint | 2.12+ | `hadolint --version` | 见下方安装说明 |

### 安装 hadolint

**Windows (推荐使用 Scoop):**

```powershell
scoop install hadolint
```

**Linux:**

```bash
wget -O /usr/local/bin/hadolint https://github.com/hadolint/hadolint/releases/latest/download/hadolint-Linux-x86_64
chmod +x /usr/local/bin/hadolint
```

**macOS:**

```bash
brew install hadolint
```

**Docker 方式（所有平台）:**

```bash
docker pull hadolint/hadolint
```

> **注意**：脚本会自动检测并提示安装，支持 Docker 容器运行模式。

## 🚀 使用方法

### 方法 1: 使用 AI 助手调用

```
"使用 docker-lint skill 检查我的 Dockerfile"
```

### 方法 2: 直接运行脚本

**检查单个 Dockerfile:**

```powershell
# Windows
.\.agent\skills\docker-lint\scripts\lint.ps1

# Linux/Mac
./.agent/skills/docker-lint/scripts/lint.sh
```

**检查指定文件:**

```powershell
# Windows
.\.agent\skills\docker-lint\scripts\lint.ps1 -File ".\docker\Dockerfile.prod"

# Linux/Mac
./.agent/skills/docker-lint/scripts/lint.sh docker/Dockerfile.prod
```

**检查目录下所有 Dockerfile:**

```powershell
# Windows
.\.agent\skills\docker-lint\scripts\lint.ps1 -Path ".\containers" -Recursive

# Linux/Mac
./.agent/skills/docker-lint/scripts/lint.sh -r containers/
```

## 🎯 检查内容

### 安全性检查

- ✅ **DL3002**: 禁止使用 root 用户运行容器
- ✅ **DL3008**: 固定 apt-get 包版本
- ✅ **DL3013**: 固定 pip 包版本
- ✅ **DL3059**: 多阶段构建健康检查
- ✅ **SC2046**: Shell 脚本注入防护

### 性能优化

- ✅ **DL3003**: 使用 `WORKDIR` 代替 `cd`
- ✅ **DL3009**: 清理 apt 缓存
- ✅ **DL3015**: 避免不必要的包更新
- ✅ **DL3020**: 使用 `COPY` 代替 `ADD`
- ✅ **DL3045**: Layer 缓存优化

### 规范遵循

- ✅ **DL3006**: 指定基础镜像标签
- ✅ **DL3007**: 避免使用 `latest` 标签
- ✅ **DL3025**: 使用 JSON 格式 CMD/ENTRYPOINT
- ✅ **DL4000**: `MAINTAINER` 已弃用

## 📊 输出示例

```
🐳 Docker Lint - 正在检查 Dockerfile...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📁 文件: Dockerfile
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dockerfile:1 DL3006 warning: Always tag the version of an image explicitly
FROM python:3
     ^


Dockerfile:5 DL3008 warning: Pin versions in apt-get install
RUN apt-get update && apt-get install -y git
                                         ^


Dockerfile:15 DL3002 error: Last USER should not be root
USER root
^

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 检查结果:
   ❌ 错误: 1 个
   ⚠️  警告: 2 个
   💡 提示: 0 个
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 建议:
1. 固定基础镜像版本: FROM python:3.11-slim
2. 固定 apt 包版本: git=1:2.34.1-1ubuntu1.10
3. 使用非 root 用户: USER appuser
```

## ⚙️ 配置文件

在项目根目录创建 `.hadolint.yaml` 自定义规则：

```yaml
# .hadolint.yaml
ignored:
  - DL3008  # 允许不固定 apt 包版本（开发环境）

trustedRegistries:
  - docker.io
  - gcr.io
  - ghcr.io

label-schema:
  author: email
  version: semver

# 自定义严重性
override:
  error:
    - DL3002  # root 用户为错误级别
  warning:
    - DL3008  # 未固定版本为警告级别
  info:
    - DL3015  # 包更新建议为提示级别
```

## 🛠️ Dockerfile 修复示例

**问题 Dockerfile:**

```dockerfile
FROM python:3
RUN apt-get update && apt-get install -y git
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
USER root
CMD python app.py
```

**修复后 Dockerfile:**

```dockerfile
# 固定基础镜像版本
FROM python:3.11-slim

# 创建非 root 用户
RUN groupadd -r appuser && useradd -r -g appuser appuser

# 固定包版本并清理缓存
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git=1:2.34.1-1ubuntu1.10 && \
    rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 先复制依赖文件（利用缓存）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 再复制应用代码
COPY --chown=appuser:appuser . .

# 切换到非 root 用户
USER appuser

# 使用 JSON 格式
CMD ["python", "app.py"]
```

## 🔗 CI/CD 集成

### GitHub Actions

```yaml
name: Lint Dockerfile
on: [push, pull_request]

jobs:
  hadolint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hadolint/hadolint-action@v3.1.0
        with:
          dockerfile: Dockerfile
```

### GitLab CI

```yaml
hadolint:
  image: hadolint/hadolint:latest-alpine
  script:
    - hadolint Dockerfile
```

## 🆘 常见问题

**Q: hadolint 未安装怎么办？**  
A: 脚本会自动尝试使用 Docker 运行 hadolint 容器

**Q: 如何忽略特定规则？**  
A: 在 Dockerfile 中添加注释：

```dockerfile
# hadolint ignore=DL3008
RUN apt-get install -y git
```

**Q: 支持多阶段构建吗？**  
A: 完全支持，hadolint 会检查每个阶段的最佳实践

**Q: 可以检查 docker-compose.yml 吗？**  
A: hadolint 专注于 Dockerfile，docker-compose 使用 `docker-compose config --quiet` 验证
