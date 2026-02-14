---
name: k8s-lint
description: Kubernetes YAML validation - Use kube-linter and kubeconform to check K8s config security and best practices
---

# Kubernetes Lint Skill

## 📋 Overview

This skill uses **kube-linter** and **kubeconform** for dual validation of Kubernetes YAML configurations, ensuring:

- 🔒 Security (RBAC, Pod Security, NetworkPolicy)
- ✅ Schema validation (K8s API spec compliance)
- ⚡ Resource limit configuration
- 🛡️ Best practices compliance

## 🔧 Prerequisites

| Tool | Purpose | Windows | Linux/Mac |
|------|---------|---------|-----------|
| kube-linter | Best practices check | `scoop install kube-linter` | `brew install kube-linter` |
| kubeconform | Schema validation | `scoop install kubeconform` | `brew install kubeconform` |
| kubectl | (Optional) Cluster validation | `scoop install kubectl` | `brew install kubectl` |

## 🚀 Usage

**Check single file:**

```powershell
# Windows
.\.agents\skills\k8s-lint\scripts\lint.ps1 -File deployment.yaml

# Linux/Mac
./agent/skills/k8s-lint/scripts/lint.sh deployment.yaml
```

**Check entire directory:**

```powershell
# Windows  
.\.agents\skills\k8s-lint\scripts\lint.ps1 -Path .\k8s -Recursive

# Linux/Mac
./.agents/skills/k8s-lint/scripts/lint.sh -r k8s/
```

## 🎯 What It Checks

### Security Checks

- ✅ Prohibit privileged containers
- ✅ Prohibit hostNetwork/hostPID
- ✅ Require readOnlyRootFilesystem
- ✅ Run as non-root user
- ✅ Capabilities whitelist

### Resource Management

- ✅ CPU/Memory limits set
- ✅ liveness/readiness probes
- ✅ Pod Disruption Budget
- ✅ HPA configuration check

### Best Practices

- ✅ Image pull policy
- ✅ Don't use latest tag
- ✅ Service Account configuration
- ✅ Label/Annotation standards

## 📊 Output Example

```
☸️  Kubernetes Lint - Checking config files...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 Schema Validation (kubeconform)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ deployment.yaml - valid
✅ service.yaml - valid
❌ ingress.yaml - invalid: Missing required field: spec.rules

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛡️  Best Practices Check (kube-linter)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

deployment.yaml: (object: <no namespace>/nginx-deployment apps/v1, Kind=Deployment)
    ⚠️  no-read-only-root-fs: Container "nginx" does not have a read-only root file system
    ❌ cpu-requirements: Container "nginx" has no CPU limits
    ❌ memory-requirements: Container "nginx" has no memory limits

📊 Check Results:
   ❌ Errors: 3
   ⚠️  Warnings: 1
```

## ⚙️ Configuration

Create `.kube-linter.yaml`:

```yaml
checks:
  exclude:
    - no-read-only-root-fs  # Temporarily allow writable root filesystem
  
  include:
    - cpu-requirements
    - memory-requirements
    - privileged-containers
    - run-as-non-root

customChecks: []
```

## 🔗 Related Resources

- [kube-linter Documentation](https://docs.kubelinter.io/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)

