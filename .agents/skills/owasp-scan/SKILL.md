---
name: owasp-scan
description: OWASP dependency vulnerability scan - Use OWASP Dependency-Check to detect known CVE vulnerabilities in project dependencies
---

# OWASP Security Scan Skill

## 📋 Overview

Use **OWASP Dependency-Check** to scan project dependencies, detecting:

- 🔒 Known CVE vulnerabilities
- 📊 NVD database comparison
- 📋 Compliance report generation
- 🚨 High-risk vulnerability alerts

## 🔧 Prerequisites

| Tool | Min Version | Installation |
|------|-------------|--------------|
| Java | 11+ | [adoptium.net](https://adoptium.net/) |
| OWASP Dependency-Check | 12.0+ | [Download CLI](https://github.com/jeremylong/DependencyCheck/releases) |

**Optional**: Apply for [NVD API Key](https://nvd.nist.gov/developers/request-an-api-key) to speed up scanning

## 🚀 Usage

**Scan current project:**

```bash
.\.agent\skills\owasp-scan\scripts\scan.ps1
```

**Specify scan directory:**

```bash
.\.agent\skills\owasp-scan\scripts\scan.ps1 -Path .\src
```

**Use NVD API Key:**

```bash
$env:NVD_API_KEY = "your-api-key"
.\.agent\skills\owasp-scan\scripts\scan.ps1
```

**Generate HTML report:**

```bash
.\.agent\skills\owasp-scan\scripts\scan.ps1 -Format html
```

## 🎯 Detection Scope

### Supported Languages/Tools

- ✅ Python (pip, pipenv, poetry)
- ✅ JavaScript/TypeScript (npm, yarn, pnpm)
- ✅ Java (Maven, Gradle)
- ✅ .NET (NuGet)
- ✅ Ruby (Bundler)
- ✅ Go (go.mod)
- ✅ PHP (Composer)

### Scan Content

- CVE vulnerability IDs
- CVSS scores (2.0 / 3.x)
- Affected version ranges
- Recommended fix versions

## 📊 Output Example

```
🔒 OWASP Dependency-Check - Scanning project dependencies...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Dependencies found: 45
🔍 Scanning vulnerability database...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ CRITICAL (CVSS 9.8)
   Package: requests@2.25.0
   CVE: CVE-2023-32681
   Description: Unintended leak of Proxy-Authorization header
   Recommendation: Upgrade to requests >= 2.31.0

⚠️  HIGH (CVSS 7.5)  
   Package: django@3.2.0
   CVE: CVE-2023-31047
   Description: Potential denial-of-service in file uploads
   Recommendation: Upgrade to django >= 3.2.19

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Scan Results:
   ❌ Critical: 1
   ⚠️  High: 1
   ⚠️  Medium: 3
   💡 Low: 2

📄 Detailed report: ./dependency-check-report.html
```

## ⚙️ Configuration

Create `dependency-check.properties`:

```properties
# NVD API Key
nvd.api.key=${NVD_API_KEY}

# Suppress false positives
suppression.file=./dependency-suppression.xml

# Scan timeout (seconds)
connection.timeout=30

# Only report specific severity levels
failBuildOnCVSS=7.0

# Project name
project=MyProject
```

Create false positive suppression file `dependency-suppression.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<suppressions xmlns="https://jeremylong.github.io/DependencyCheck/dependency-suppression.1.3.xsd">
    <!-- Suppress specific CVE -->
    <suppress>
        <notes>False positive - not using vulnerable functionality</notes>
        <cve>CVE-2023-12345</cve>
    </suppress>
    
    <!-- Suppress specific package -->
    <suppress>
        <notes>Dev dependency only</notes>
        <gav regex="true">^org\.example:test-utils:.*$</gav>
    </suppress>
</suppressions>
```

## 🔄 CI/CD Integration

### GitHub Actions

```yaml
name: OWASP Dependency Check
on: [push, pull_request]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run OWASP Dependency-Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: 'MyProject'
          path: '.'
          format: 'HTML'
        env:
          NVD_API_KEY: ${{ secrets.NVD_API_KEY }}
      
      - name: Upload Report
        uses: actions/upload-artifact@v4
        with:
          name: dependency-check-report
          path: dependency-check-report.html
```

## 🆘 FAQ

**Q: Is NVD API Key required?**  
A: Not required but strongly recommended. Without API Key, updates are slow (<10 req/min)

**Q: How to handle false positives?**  
A: Use `dependency-suppression.xml` file to suppress false positives

**Q: Scan is slow, what can I do?**  
A: 1) Use NVD API Key  2) Cache NVD database  3) Incremental scan

**Q: Does it support private repositories?**  
A: Yes, but private library vulnerability info needs to be public in NVD

## 🔗 Related Resources

- [OWASP Dependency-Check Official](https://owasp.org/www-project-dependency-check/)
- [NVD Database](https://nvd.nist.gov/)
- [CVE Details](https://cve.mitre.org/)
