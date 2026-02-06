---
name: k8s-lint
description: Kubernetes YAML 验证 - 使用 kube-linter 和 kubeconform 检查 K8s 配置安全性和最佳实践
---

# Kubernetes Lint Skill

## 📋 概述

此 skill 使用 **kube-linter** 和 **kubeconform** 双重验证 Kubernetes YAML 配置，确保：

- 🔒 安全性（RBAC、Pod Security、NetworkPolicy）
- ✅ Schema 验证（符合 K8s API 规范）
- ⚡ 资源限制配置
- 🛡️ 最佳实践遵循

## 🔧 前置条件 (Prerequisites)

| 工具 | 用途 | 安装命令 (Windows) | 安装命令 (Linux/Mac) |
|-----|------|-----------------|------------------|
| kube-linter | 最佳实践检查 | `scoop install kube-linter` | `brew install kube-linter` |
| kubeconform | Schema 验证 | `scoop install kubeconform` | `brew install kubeconform` |
| kubectl | (可选) 集群验证 | `scoop install kubectl` | `brew install kubectl` |

## 🚀 使用方法

**检查单个文件:**

```powershell
# Windows
.\.agent\skills\k8s-lint\scripts\lint.ps1 -File deployment.yaml

# Linux/Mac
./agent/skills/k8s-lint/scripts/lint.sh deployment.yaml
```

**检查整个目录:**

```powershell
# Windows  
.\.agent\skills\k8s-lint\scripts\lint.ps1 -Path .\k8s -Recursive

# Linux/Mac
./.agent/skills/k8s-lint/scripts/lint.sh -r k8s/
```

## 🎯 检查内容

### 安全检查

- ✅ 禁止 privileged 容器
- ✅ 禁止 hostNetwork/hostPID
- ✅ 要求 readOnlyRootFilesystem
- ✅ 非 root 用户运行
- ✅ capabilities 白名单

### 资源管理

- ✅ CPU/Memory limits 设置
- ✅ liveness/readiness probes
- ✅ Pod Disruption Budget
- ✅ HPA 配置检查

### 最佳实践

- ✅ 镜像拉取策略
- ✅ 不使用 latest 标签
- ✅ Service Account 配置
- ✅ Label/Annotation 规范

## 📊 输出示例

```
☸️  Kubernetes Lint - 检查配置文件...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 Schema 验证 (kubeconform)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ deployment.yaml - valid
✅ service.yaml - valid
❌ ingress.yaml - invalid: Missing required field: spec.rules

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛡️  最佳实践检查 (kube-linter)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

deployment.yaml: (object: <no namespace>/nginx-deployment apps/v1, Kind=Deployment)
    ⚠️  no-read-only-root-fs: Container "nginx" does not have a read-only root file system
    ❌ cpu-requirements: Container "nginx" has no CPU limits
    ❌ memory-requirements: Container "nginx" has no memory limits

📊 检查结果:
   ❌ 错误: 3 个
   ⚠️  警告: 1 个
```

## ⚙️ 配置文件

创建 `.kube-linter.yaml`:

```yaml
checks:
  exclude:
    - no-read-only-root-fs  # 暂时允许可写根文件系统
  
  include:
    - cpu-requirements
    - memory-requirements
    - privileged-containers
    - run-as-non-root

customChecks: []
```

## 🔗 相关资源

- [kube-linter 文档](https://docs.kubelinter.io/)
- [Kubernetes 最佳实践](https://kubernetes.io/docs/concepts/configuration/overview/)
