---
name: security-check
description: Check dependency security vulnerabilities
---

# Security Vulnerability Check Skill

## 📋 Overview

Check project dependencies for known security vulnerabilities, supporting multiple languages and package managers:

- 🔒 **CVE Database**: Detect known vulnerabilities
- 📊 **Severity Scoring**: CVSS scoring system
- 🔧 **Fix Recommendations**: Suggest secure versions
- 🚨 **Real-time Updates**: Latest vulnerability data

## 🔧 Prerequisites

| Language/Tool | Check Tool | Installation |
|---------------|------------|--------------|
| **Python** | pip-audit, Safety | `pip install pip-audit safety` |
| **JavaScript** | npm audit | Built into npm |
| **Java** | OWASP Dependency-Check | [Download CLI](https://github.com/jeremylong/DependencyCheck) |
| **.NET** | dotnet list package --vulnerable | Built into .NET SDK |
| **Ruby** | bundler-audit | `gem install bundler-audit` |
| **Go** | govulncheck | `go install golang.org/x/vuln/cmd/govulncheck@latest` |

## 🚀 Usage

### Method 1: Use AI Assistant

```
"Check project security vulnerabilities"
"Scan dependencies for CVEs"
"Run security audit"
```

### Method 2: Run Commands Manually

**Python:**

```bash
# Using pip-audit (recommended)
pip-audit                           # Scan current environment
pip-audit -r requirements.txt       # Scan specific file

# Using Safety
safety check                        # Scan current environment
safety check --json                 # JSON output
```

**JavaScript/Node.js:**

```bash
npm audit                           # Scan and show vulnerabilities
npm audit fix                       # Auto-fix (minor versions)
npm audit fix --force               # Force fix (may break compatibility)
npm audit --json                    # JSON output
```

**Yarn:**

```bash
yarn audit                          # Scan vulnerabilities
yarn audit --level high             # Show high severity only
```

**pnpm:**

```bash
pnpm audit                          # Scan vulnerabilities
pnpm audit --fix                    # Auto-fix
```

**Java (Maven):**

```bash
# Using OWASP Dependency-Check
mvn org.owasp:dependency-check-maven:check

# Using Snyk
snyk test
```

**.NET:**

```bash
dotnet list package --vulnerable              # List vulnerabilities
dotnet list package --vulnerable --include-transitive  # Include transitive deps
```

**Ruby:**

```bash
bundle audit check                  # Check Gemfile.lock
bundle audit update                 # Update vulnerability database
```

**Go:**

```bash
govulncheck ./...                   # Scan all packages
govulncheck -json ./...             # JSON output
```

## 🎯 What It Checks

### Vulnerability Detection

- ✅ Known CVE IDs
- ✅ CVSS scores (severity)
- ✅ Affected version ranges
- ✅ Vulnerability descriptions and links

### Dependency Analysis

- ✅ Direct dependencies
- ✅ Transitive dependencies
- ✅ Development dependencies (optional)
- ✅ License checks (some tools)

### Fix Recommendations

- ✅ Recommended secure versions
- ✅ Fix PRs (some tools)
- ✅ Workarounds (if upgrade not possible)
- ✅ Alternative package recommendations

## 📊 Output Examples

**npm audit output:**

```
found 3 vulnerabilities (1 moderate, 2 high) in 856 scanned packages
  run `npm audit fix` to fix 2 of them.
  1 vulnerability requires manual review. See the full report for details.

┌───────────────┬──────────────────────────────────────────────────────────────┐
│ High          │ Regular Expression Denial of Service in lodash              │
├───────────────┼──────────────────────────────────────────────────────────────┤
│ Package       │ lodash                                                        │
├───────────────┼──────────────────────────────────────────────────────────────┤
│ Patched in    │ >=4.17.21                                                    │
├───────────────┼──────────────────────────────────────────────────────────────┤
│ Dependency of │ express                                                       │
├───────────────┼──────────────────────────────────────────────────────────────┤
│ Path          │ express > lodash                                              │
├───────────────┼──────────────────────────────────────────────────────────────┤
│ More info     │ https://github.com/advisories/GHSA-x5rq-j2xg-h7qm           │
└───────────────┴──────────────────────────────────────────────────────────────┘
```

**pip-audit output:**

```
Found 2 known vulnerabilities in 1 package

Name    Version ID              Fix Versions
------- ------- --------------- ------------
urllib3 1.26.5  PYSEC-2021-108  1.26.5
                PYSEC-2021-59   1.26.4
```

## ⚙️ Configuration

### .npmrc (npm audit)

```ini
audit-level=high       # Only report high and above
audit=true             # Auto-check on install
```

### .safety-policy.yml (Python Safety)

```yaml
security:
  ignore-vulnerabilities:
    # Temporarily ignore specific CVE (must comment reason)
    12345:
      reason: "Verified not affecting our use case"
      expires: "2026-12-31"
  
  continue-on-vulnerability-error: false
```

## 🔄 CI/CD Integration

### GitHub Actions

```yaml
name: Security Audit
on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run npm audit
        run: npm audit --audit-level=high
        continue-on-error: true
      
      - name: Run Snyk
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

### GitLab CI

```yaml
security_scan:
  stage: test
  image: python:3.11
  script:
    - pip install pip-audit
    - pip-audit -r requirements.txt
  allow_failure: true
```

## 🆘 FAQ

**Q: What to do after finding vulnerabilities?**  
A:

1. Assess severity (CVSS score)
2. Check if it affects your use case
3. Upgrade to fixed version
4. If upgrade not possible, find alternatives or mitigations

**Q: What if `npm audit fix` breaks compatibility?**  
A:

1. First run `npm audit` to see details
2. Manually upgrade specific packages: `npm update package-name`
3. Use `npm audit fix --dry-run` to preview
4. Test before committing

**Q: How to ignore specific vulnerabilities?**  
A:

- npm: Use `npm audit fix --force` or `.auditrc`
- Python: Add exceptions in `.safety-policy.yml`
- **Note**: Must have valid reason and review regularly

**Q: CI/CD security check failures causing build failures?**  
A:

1. Set severity threshold (e.g., only high/critical fail)
2. Use `continue-on-error: true` as warning
3. Fix vulnerabilities regularly, don't accumulate

**Q: How to prevent introducing vulnerabilities?**  
A:

1. Pre-commit hook running security checks
2. Auto-run audit in PRs
3. Use tools like Snyk/Dependabot for auto PRs
4. Regularly update dependencies

## 🔗 Related Resources

- [npm audit Documentation](https://docs.npmjs.com/cli/audit)
- [pip-audit GitHub](https://github.com/pypa/pip-audit)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
- [Snyk Vulnerability Database](https://snyk.io/vuln/)
- [CVE Details](https://cve.mitre.org/)
- [NVD Database](https://nvd.nist.gov/)
