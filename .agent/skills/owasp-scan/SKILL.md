---
name: owasp-scan
description: OWASP 依赖漏洞扫描 - 使用 OWASP Dependency-Check 检测项目依赖中的已知 CVE 漏洞
---

# OWASP Security Scan Skill

## 📋 概述

使用 **OWASP Dependency-Check** 扫描项目依赖，检测：

- 🔒 已知 CVE 漏洞
- 📊 NVD 数据库对比
- 📋 合规性报告生成
- 🚨 高危漏洞告警

## 🔧 前置条件

| 工具 | 最低版本 | 安装 |
|-----|---------|-----|
| Java | 11+ | [adoptium.net](https://adoptium.net/) |
| OWASP Dependency-Check | 12.0+ | [下载 CLI](https://github.com/jeremylong/DependencyCheck/releases) |

**可选**: 申请 [NVD API Key](https://nvd.nist.gov/developers/request-an-api-key) 加速扫描

## 🚀 使用方法

**扫描当前项目:**

```bash
.\.agent\skills\owasp-scan\scripts\scan.ps1
```

**指定扫描目录:**

```bash
.\.agent\skills\owasp-scan\scripts\scan.ps1 -Path .\src
```

**使用 NVD API Key:**

```bash
$env:NVD_API_KEY = "your-api-key"
.\.agent\skills\owasp-scan\scripts\scan.ps1
```

**生成 HTML 报告:**

```bash
.\.agent\skills\owasp-scan\scripts\scan.ps1 -Format html
```

## 🎯 检测范围

### 支持的语言/工具

- ✅ Python (pip, pipenv, poetry)
- ✅ JavaScript/TypeScript (npm, yarn, pnpm)
- ✅ Java (Maven, Gradle)
- ✅ .NET (NuGet)
- ✅ Ruby (Bundler)
- ✅ Go (go.mod)
- ✅ PHP (Composer)

### 扫描内容

- CVE 漏洞编号
- CVSS 评分（2.0 / 3.x）
- 受影响版本范围
- 修复建议版本

## 📊 输出示例

```
🔒 OWASP Dependency-Check - 扫描项目依赖...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 发现依赖: 45 个
🔍 扫描漏洞数据库...
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
📊 扫描结果:
   ❌ Critical: 1 个
   ⚠️  High: 1 个
   ⚠️  Medium: 3 个
   💡 Low: 2 个

📄 详细报告: ./dependency-check-report.html
```

## ⚙️ 配置文件

创建 `dependency-check.properties`:

```properties
# NVD API Key
nvd.api.key=${NVD_API_KEY}

# 抑制误报
suppression.file=./dependency-suppression.xml

# 扫描超时（秒）
connection.timeout=30

# 仅报告特定严重级别
failBuildOnCVSS=7.0

# 工程名称
project=MyProject
```

创建误报抑制文件 `dependency-suppression.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<suppressions xmlns="https://jeremylong.github.io/DependencyCheck/dependency-suppression.1.3.xsd">
    <!-- 抑制特定CVE -->
    <suppress>
        <notes>False positive - not using vulnerable functionality</notes>
        <cve>CVE-2023-12345</cve>
    </suppress>
    
    <!-- 抑制特定包 -->
    <suppress>
        <notes>Dev dependency only</notes>
        <gav regex="true">^org\.example:test-utils:.*$</gav>
    </suppress>
</suppressions>
```

## 🔄 CI/CD 集成

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

## 🆘 常见问题

**Q: NVD API Key 是必须的吗？**  
A: 不是必须，但强烈推荐。没有 API Key 时更新会很慢（<10 req/min）

**Q: 如何处理误报？**  
A: 使用 `dependency-suppression.xml` 文件抑制误报

**Q: 扫描速度慢怎么办？**  
A: 1) 使用 NVD API Key  2) 缓存 NVD 数据库  3) 增量扫描

**Q: 支持私有库吗？**  
A: 支持，但私有库漏洞信息需要在 NVD 中公开

## 🔗 相关资源

- [OWASP Dependency-Check 官网](https://owasp.org/www-project-dependency-check/)
- [NVD 数据库](https://nvd.nist.gov/)
- [CVE 详情](https://cve.mitre.org/)
