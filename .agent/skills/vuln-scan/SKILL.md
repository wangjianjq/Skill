---
name: vuln-scan
description: Multi-language dependency security scan - Use Safety CLI and OSV-Scanner to quickly detect dependency vulnerabilities in Python/JS/Java projects
---

# Vulnerability Scanner Skill

## 📋 Overview

Provides two lightweight vulnerability scanning tools:

- **Safety CLI**: Python/JS/Java smart scanning (AI enhanced)
- **OSV-Scanner**: Google open source, supports multiple ecosystems

## 🔧 Prerequisites

| Tool | Installation (All Platforms) |
|------|------------------------------|
| Safety CLI | `pip install safety` |
| OSV-Scanner | [Download](https://github.com/google/osv-scanner/releases) |

## 🚀 Usage

**Safety CLI Scan:**

```bash
# Windows
.\.agent\skills\vuln-scan\scripts\safety-scan.ps1

# Linux/Mac
./.agent/skills/vuln-scan/scripts/safety-scan.sh
```

**OSV-Scanner Scan:**

```bash
# Windows
.\.agent\skills\vuln-scan\scripts\osv-scan.ps1

# Linux/Mac
./.agent/skills/vuln-scan/scripts/osv-scan.sh
```

**CI/CD Mode:**

```bash
.\.agent\skills\vuln-scan\scripts\safety-scan.ps1 -CI
# Sets exit code, breaks pipeline on failure
```

## 🎯 Scan Coverage

### Safety CLI Support

- ✅ Python (requirements.txt, Pipfile, pyproject.toml)
- ✅ JavaScript/TypeScript (package.json, package-lock.json)
- ✅ Java (pom.xml, build.gradle)

### OSV-Scanner Support

- ✅ Python, JavaScript, TypeScript
- ✅ Java, Go, Rust
- ✅ Ruby, PHP, C/C++
- ✅ And 20+ other ecosystems

## 📊 Output Example

```
🔍 Vulnerability Scan - Safety CLI

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Scanning: requirements.txt (23 dependencies)
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
📊 Scan Results:
   🔴 Critical: 0
   🟠 High: 1
   🟡 Medium: 2
   🟢 Low: 0

💡 Fix Suggestion:
   pip install --upgrade urllib3>=1.26.18
```

## ⚙️ Configuration

### Safety CLI (`.safety-policy.yml`)

```yaml
# Security policy config
security:
  # Ignore specific vulnerability IDs
  ignore-vulnerabilities:
    51499:
      reason: "False positive - not using affected functionality"
      expires: "2026-12-31"
  
  # Ignore specific packages
  ignore-packages:
    - package: test-utils
      reason: "Dev dependency only"
  
  # Set CVSS threshold
  continue-on-vulnerability-error: false
  fail-security-check-threshold: 7.0

# Monitoring config
alert:
  # Optional: Integrate Slack/Email alerts
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

## 🔄 Auto-fix

**Safety CLI Auto-upgrade:**

```bash
# Generate fix commands
safety check --json | safety generate fixes

# Or apply fixes directly (use with caution)
safety check --apply-fixes
```

**Manual Fix Examples:**

```bash
# Python
pip install --upgrade package-name>=safe-version

# JavaScript
npm update package-name@safe-version

# Java (Maven)
# Modify version in pom.xml
```

## 🔗 CI/CD Integration

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

## 🆘 FAQ

**Q: Does Safety CLI require an API Key?**  
A: Free version has limits, recommend applying for free API Key: [safety.com](https://safetycli.com/)

**Q: OSV-Scanner vs Safety CLI?**  
A:  

- **OSV-Scanner**: Wider language support, community-driven
- **Safety CLI**: Stronger Python ecosystem, AI-enhanced detection

**Q: How to use in offline environments?**  
A: Safety CLI can download offline database; OSV-Scanner supports local caching

**Q: Too many false positives?**  
A: Use config files to suppress known false positives, keep reason notes

## 🔗 Related Resources

- [Safety CLI Documentation](https://docs.safetycli.com/)
- [OSV-Scanner GitHub](https://github.com/google/osv-scanner)
- [OSV Vulnerability Database](https://osv.dev/)
