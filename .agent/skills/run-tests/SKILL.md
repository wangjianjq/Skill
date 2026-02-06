---
name: run-tests
description: 运行项目测试套件
---

# Run Tests Skill

## 📋 概述

智能运行项目测试套件，自动检测测试框架并执行：

- 🔍 **自动检测**：识别 Jest、Pytest、Mocha、JUnit 等
- 📊 **覆盖率报告**：生成代码覆盖率统计
- ⚡ **并行执行**：加速测试运行
- 🎯 **选择性测试**：支持运行特定测试

## 🔧 前置条件 (Prerequisites)

| 框架 | 语言 | 检测文件 | 安装命令 |
|------|------|---------|---------|
| **Pytest** | Python | `pytest.ini`, `test_*.py` | `pip install pytest pytest-cov` |
| **Jest** | JavaScript | `jest.config.js`, `*.test.js` | `npm install --save-dev jest` |
| **Mocha** | JavaScript | `mocha.opts`, `test/` | `npm install --save-dev mocha` |
| **JUnit** | Java | `pom.xml`, `build.gradle` | Maven/Gradle 自带 |
| **Go Test** | Go | `*_test.go` | Go 内置 |

> **注意**：AI 会自动检测项目使用的测试框架

## 🚀 使用方法

### 方法 1: 使用 AI 助手调用

```
"运行项目测试"
"执行所有单元测试"
"运行测试并生成覆盖率报告"
```

### 方法 2: 手动运行命令

**Python (Pytest):**

```bash
pytest                          # 运行所有测试
pytest --cov=.                  # 生成覆盖率
pytest tests/test_api.py        # 运行特定文件
pytest -k "test_login"          # 运行匹配的测试
pytest -v                       # 详细输出
```

**JavaScript (Jest):**

```bash
npm test                        # 运行所有测试
npm test -- --coverage          # 生成覆盖率
npm test -- api.test.js         # 运行特定文件
npm test -- -t "login"          # 运行匹配的测试
jest --watch                    # 监听模式
```

**JavaScript (Mocha):**

```bash
npm test                        # 运行所有测试
mocha test/                     # 指定目录
mocha test/**/*.test.js         # 使用 glob
mocha --reporter spec           # 指定报告格式
```

**Java (Maven):**

```bash
mvn test                        # 运行所有测试
mvn test -Dtest=ApiTest         # 运行特定测试类
mvn test -DfailIfNoTests=false  # 无测试不失败
```

**Go:**

```bash
go test ./...                   # 运行所有包的测试
go test -v ./...                # 详细输出
go test -cover ./...            # 覆盖率
go test -run TestLogin          # 运行特定测试
```

## 🎯 测试类型

### 单元测试

- ✅ 函数/方法级别测试
- ✅ 隔离依赖（Mock/Stub）
- ✅ 快速执行
- ✅ 高覆盖率目标

### 集成测试

- ✅ 多组件交互测试
- ✅ 数据库/API 集成
- ✅ 端到端流程
- ✅ 环境依赖

### 性能测试

- ✅ 响应时间测试
- ✅ 负载测试
- ✅ 压力测试
- ✅ 基准测试

## 📊 输出示例

**Pytest 输出:**

```
================================= test session starts ==================================
platform win32 -- Python 3.11.7, pytest-7.4.3
rootdir: C:\Project
plugins: cov-4.1.0
collected 45 items

tests/test_api.py ........                                                  [ 17%]
tests/test_auth.py .....                                                    [ 29%]
tests/test_database.py ..........                                           [ 51%]
tests/test_utils.py ....................                                    [100%]

---------- coverage: platform win32, python 3.11.7 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
src/api.py              120      5    96%
src/auth.py              85      0   100%
src/database.py         150     12    92%
src/utils.py             95      3    97%
-----------------------------------------
TOTAL                   450     20    96%

============================== 45 passed in 2.34s ==================================
```

**Jest 输出:**

```
PASS  tests/api.test.js
PASS  tests/auth.test.js
PASS  tests/utils.test.js

Test Suites: 3 passed, 3 total
Tests:       45 passed, 45 total
Snapshots:   0 total
Time:        3.421 s
Ran all test suites.

----------------------|---------|----------|---------|---------|-------------------
File                  | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
----------------------|---------|----------|---------|---------|-------------------
All files             |   94.2  |   88.5   |   96.3  |   94.8  |
 api.js               |   96.5  |   90.2   |  100.0  |   97.1  | 45,78
 auth.js              |  100.0  |  100.0   |  100.0  |  100.0  |
 utils.js             |   89.4  |   82.1   |   91.7  |   90.2  | 23,45-48,92
----------------------|---------|----------|---------|---------|-------------------
```

## ⚙️ 配置文件

### Pytest (pytest.ini)

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --cov=src
    --cov-report=html
    --cov-report=term
    --cov-fail-under=80
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
```

### Jest (jest.config.js)

```javascript
module.exports = {
  testEnvironment: 'node',
  coverageDirectory: 'coverage',
  collectCoverageFrom: [
    'src/**/*.{js,ts}',
    '!src/**/*.test.{js,ts}',
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
  testMatch: [
    '**/__tests__/**/*.[jt]s?(x)',
    '**/?(*.)+(spec|test).[jt]s?(x)',
  ],
};
```

### Mocha (.mocharc.json)

```json
{
  "require": ["chai"],
  "spec": "test/**/*.test.js",
  "reporter": "spec",
  "timeout": 5000,
  "recursive": true
}
```

## �� CI/CD 集成

### GitHub Actions

```yaml
name: Run Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      
      - name: Run tests
        run: pytest --cov=src --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
```

### GitLab CI

```yaml
test:
  stage: test
  image: python:3.11
  script:
    - pip install -r requirements.txt pytest pytest-cov
    - pytest --cov=src --cov-report=term
  coverage: '/TOTAL.*\s+(\d+%)$/'
```

## 🆘 常见问题

**Q: 如何只运行失败的测试？**  
A:

- Pytest: `pytest --lf` (last failed)
- Jest: `jest --onlyFailures`

**Q: 如何跳过慢速测试？**  
A:

- Pytest: 使用 marker `@pytest.mark.slow` 然后 `pytest -m "not slow"`
- Jest: 使用 `test.skip()` 或 `--testPathIgnorePatterns`

**Q: 如何并行运行测试？**  
A:

- Pytest: `pip install pytest-xdist` 然后 `pytest -n auto`
- Jest: 默认并行，使用 `--maxWorkers=4` 调整

**Q: 测试覆盖率低怎么办？**  
A:

1. 识别未覆盖代码：查看 HTML 报告
2. 编写缺失的测试
3. 重构复杂函数提高可测试性

**Q: 测试运行很慢怎么办？**  
A:

1. 使用并行执行
2. Mock 外部依赖（数据库、API）
3. 分离快速和慢速测试

## 🔗 相关资源

- [Pytest 文档](https://docs.pytest.org/)
- [Jest 文档](https://jestjs.io/)
- [Mocha 文档](https://mochajs.org/)
- [测试最佳实践](https://martinfowler.com/testing/)
