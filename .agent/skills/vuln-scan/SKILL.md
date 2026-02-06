---
name: vuln-scan
description: 多语言依赖安全扫描 - 使用 Safety CLI 和 OSV-Scanner 快速检测 Python/JS/Java 项目的依赖漏洞
---

# Vulnerability Scanner Skill

## 📋 概述

提供两种轻量级漏洞扫描工具：

- **Safety CLI**: Python/JS/Java 智能扫描（AI 增强）
- **OSV-Scanner**: Google 开源，支持多种生态系统

## 🔧 前置条件

| 工具 | 安装命令 (所有平台) |
|-----|-----------------|
| Safety CLI | `pip install safety` |
| OSV-Scanner | [下载](https://github.com/google/osv-scanner/releases) |

## 🚀 使用方法

**Safety CLI 扫描:**

```bash
# Windows
.\.agent\skills\vuln-scan\scripts\safety-scan.ps1

# Linux/Mac
./.agent/skills/vuln-scan/scripts/safety-scan.sh
```

**OSV-Scanner 扫描:**

```bash
# Windows
.\.agent\skills\vuln-scan\scripts\osv-scan.ps1

# Linux/Mac
./.agent/skills/vuln-scan/scripts/osv-scan.sh
```

**CI/CD 模式:**

```bash
.\.agent\skills\vuln-scan\scripts\safety-scan.ps1 -CI
# 设置退出码，失败时中断流水线
```

## 🎯 扫描范围

### Safety CLI 支持

- ✅ Python (requirements.txt, Pipfile, pyproject.toml)
- ✅ JavaScript/TypeScript (package.json, package-lock.json)
- ✅ Java (pom.xml, build.gradle)

### OSV-Scanner 支持

- ✅ Python, JavaScript, TypeScript
- ✅ Java, Go, Rust
- ✅ Ruby, PHP, C/C++
- ✅ 以及其他 20+ 生态系统

## 📊 输出示例

```
🔍 Vulnerability Scan - Safety CLI

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 扫描: requirements.txt (23 个依赖)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╭────────────────────────────────────────╮
│ ❌ VULNERABILITY FOUND                 │
├────────────────────────────────────────┤
│ Package: urllib3                       │
│ Installed: 1.26.5                      │
│ Affected: <1.26.18                     │
│ ID: 51499                              │
│                                        │
│ OWASP Top 10: A05:2021 - Security      │
│ Misconfiguration                       │
│                                        │
│ Description:                           │
│ urllib3's request body can leak from   │
│ URLError exceptions                    │
│                                        │
│ Fix: Upgrade to urllib3>=1.26.18       │
╰────────────────────────────────────────╯

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 扫描结果:
   🔴 Critical: 0 个
   🟠 High: 1 个
   🟡 Medium: 2 个
   🟢 Low: 0 个

💡 修复建议:
   pip install --upgrade urllib3>=1.26.18
```

## ⚙️ 配置文件

### Safety CLI (`.safety-policy.yml`)

```yaml
# 安全策略配置
security:
  # 忽略特定漏洞ID
  ignore-vulnerabilities:
    51499:
      reason: "False positive - not using affected functionality"
      expires: "2026-12-31"
  
  # 忽略特定包
  ignore-packages:
    - package: test-utils
      reason: "Dev dependency only"
  
  # 设置 CVSS 阈值
  continue-on-vulnerability-error: false
  fail-security-check-threshold: 7.0

# 监控配置
alert:
  # 可选：集成 Slack/Email 告警
  on-vulnerability: slack
  webhook: ${SAFETY_WEBHOOK_URL}
```

### OSV-Scanner (osv-scanner.toml)

```toml
[[IgnoredVulns]]
id = "GHSA-xxxx-yyyy-zzzz"
reason = "Not applicable to our use case"

[[PackageOverrides]]
name = "example"
version = "1.0.0"
ecosystem = "npm"
ignore = true
```

## 🔄 自动修复

**Safety CLI 自动升级:**

```bash
# 生成修复命令
safety check --json | safety generate fixes

# 或直接应用修复（谨慎使用）
safety check --apply-fixes
```

**手动修复示例:**

```bash
# Python
pip install --upgrade package-name>=safe-version

# JavaScript
npm update package-name@safe-version

# Java (Maven)
# 修改 pom.xml 中的版本号
```

## 🔗 CI/CD 集成

### GitHub Actions (Safety CLI)

```yaml
name: Security Scan
on: [push, pull_request]

jobs:
  safety-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install Safety
        run: pip install safety
      
      - name: Run Safety Check
        run: safety check --json
        env:
          SAFETY_API_KEY: ${{ secrets.SAFETY_API_KEY }}
```

### GitLab CI (OSV-Scanner)

```yaml
osv-scan:
  image: golang:latest
  script:
    - go install github.com/google/osv-scanner/cmd/osv-scanner@latest
    - osv-scanner --lockfile=package-lock.json
```

## 🆘 常见问题

**Q: Safety CLI 需要 API Key 吗？**  
A: 免费版有限制，推荐申请免费 API Key：[safety.com](https://safetycli.com/)

**Q: OSV-Scanner vs Safety CLI？**  
A:  

- **OSV-Scanner**: 更广泛的语言支持，社区驱动
- **Safety CLI**: Python 生态更强，AI 增强检测

**Q: 如何在离线环境使用？**  
A: Safety CLI 可下载离线数据库；OSV-Scanner 支持本地缓存

**Q: 误报太多怎么办？**  
A: 使用配置文件抑制已知误报，并保留原因说明

## 🔗 相关资源

- [Safety CLI 官方文档](https://docs.safetycli.com/)
- [OSV-Scanner GitHub](https://github.com/google/osv-scanner)
- [OSV 漏洞数据库](https://osv.dev/)
