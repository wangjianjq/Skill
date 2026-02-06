---
name: security-check
description: 检查依赖项安全漏洞
---

# Security Vulnerability Check Skill

## 📋 概述

检查项目依赖项中的已知安全漏洞，支持多种语言和包管理器：

- 🔒 **CVE 数据库**：检测已知漏洞
- 📊 **严重性评分**：CVSS 评分系统
- 🔧 **修复建议**：推荐安全版本
- 🚨 **实时更新**：最新漏洞数据

## 🔧 前置条件 (Prerequisites)

| 语言/工具 | 检查工具 | 安装命令 |
|----------|---------|---------|
| **Python** | pip-audit, Safety | `pip install pip-audit safety` |
| **JavaScript** | npm audit | npm 内置 |
| **Java** | OWASP Dependency-Check | [下载 CLI](https://github.com/jeremylong/DependencyCheck) |
| **.NET** | dotnet list package --vulnerable | .NET SDK 内置 |
| **Ruby** | bundler-audit | `gem install bundler-audit` |
| **Go** | govulncheck | `go install golang.org/x/vuln/cmd/govulncheck@latest` |

## 🚀 使用方法

### 方法 1: 使用 AI 助手调用

```
"检查项目安全漏洞"
"扫描依赖项的 CVE"
"运行安全审计"
```

### 方法 2: 手动运行命令

**Python:**

```bash
# 使用 pip-audit（推荐）
pip-audit                           # 扫描当前环境
pip-audit -r requirements.txt       # 扫描指定文件

# 使用 Safety
safety check                        # 扫描当前环境
safety check --json                 # JSON 输出
```

**JavaScript/Node.js:**

```bash
npm audit                           # 扫描并显示漏洞
npm audit fix                       # 自动修复（小版本）
npm audit fix --force               # 强制修复（可能破坏兼容性）
npm audit --json                    # JSON 输出
```

**Yarn:**

```bash
yarn audit                          # 扫描漏洞
yarn audit --level high             # 仅显示高危
```

**pnpm:**

```bash
pnpm audit                          # 扫描漏洞
pnpm audit --fix                    # 自动修复
```

**Java (Maven):**

```bash
# 使用 OWASP Dependency-Check
mvn org.owasp:dependency-check-maven:check

# 使用 Snyk
snyk test
```

**.NET:**

```bash
dotnet list package --vulnerable              # 列出漏洞
dotnet list package --vulnerable --include-transitive  # 包括传递依赖
```

**Ruby:**

```bash
bundle audit check                  # 检查 Gemfile.lock
bundle audit update                 # 更新漏洞数据库
```

**Go:**

```bash
govulncheck ./...                   # 扫描所有包
govulncheck -json ./...             # JSON 输出
```

## 🎯 检查内容

### 漏洞检测

- ✅ 已知 CVE 编号
- ✅ CVSS 评分（严重性）
- ✅ 受影响版本范围
- ✅ 漏洞描述和链接

### 依赖分析

- ✅ 直接依赖
- ✅ 传递依赖
- ✅ 开发依赖（可选）
- ✅ 许可证检查（部分工具）

### 修复建议

- ✅ 推荐安全版本
- ✅ 修复 PR（某些工具）
- ✅ 绕过方案（如无法升级）
- ✅ 替代包推荐

## 📊 输出示例

**npm audit 输出:**

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

**pip-audit 输出:**

```
Found 2 known vulnerabilities in 1 package

Name    Version ID              Fix Versions
------- ------- --------------- ------------
urllib3 1.26.5  PYSEC-2021-108  1.26.5
                PYSEC-2021-59   1.26.4
```

## ⚙️ 配置文件

### .npmrc (npm audit)

```ini
audit-level=high       # 仅报告 high 及以上
audit=true             # 安装时自动检查
```

### .safety-policy.yml (Python Safety)

```yaml
security:
  ignore-vulnerabilities:
    # 临时忽略特定 CVE（需注释原因）
    12345:
      reason: "已验证不影响我们的使用场景"
      expires: "2026-12-31"
  
  continue-on-vulnerability-error: false
```

## 🔄 CI/CD 集成

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

## 🆘 常见问题

**Q: 发现漏洞后该怎么办？**  
A:

1. 评估严重性（CVSS 评分）
2. 检查是否影响你的使用场景
3. 升级到修复版本
4. 如无法升级，寻找替代方案或缓解措施

**Q: `npm audit fix` 破坏了兼容性怎么办？**  
A:

1. 先运行 `npm audit` 查看详情
2. 手动升级特定包：`npm update package-name`
3. 使用 `npm audit fix --dry-run` 预览
4. 测试后再提交

**Q: 如何忽略特定漏洞？**  
A:

- npm: 使用 `npm audit fix --force` 或 `.auditrc`
- Python: 在 `.safety-policy.yml` 中添加例外
- **注意**: 必须有充分理由并定期审查

**Q: CI/CD 中安全检查失败导致构建失败？**  
A:

1. 设置严重性阈值（如仅 high/critical 失败）
2. 使用 `continue-on-error: true` 作为警告
3. 定期修复漏洞，不要积累

**Q: 如何防止引入漏洞？**  
A:

1. Pre-commit hook 运行安全检查
2. PR 中自动运行审计
3. 使用工具如 Snyk/Dependabot 自动 PR
4. 定期更新依赖

## 🔗 相关资源

- [npm audit 文档](https://docs.npmjs.com/cli/audit)
- [pip-audit GitHub](https://github.com/pypa/pip-audit)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
- [Snyk 漏洞数据库](https://snyk.io/vuln/)
- [CVE 详情](https://cve.mitre.org/)
- [NVD 数据库](https://nvd.nist.gov/)
