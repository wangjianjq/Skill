---
name: run-tests
description: Run project test suite
---

# Run Tests Skill

## 📋 Overview

Intelligently run project test suites, automatically detecting test frameworks and executing:

- 🔍 **Auto-detection**: Identify Jest, Pytest, Mocha, JUnit, etc.
- 📊 **Coverage reports**: Generate code coverage statistics
- ⚡ **Parallel execution**: Speed up test runs
- 🎯 **Selective testing**: Support running specific tests

## 🔧 Prerequisites

| Framework | Language | Detection Files | Installation |
|-----------|----------|-----------------|--------------|
| **Pytest** | Python | `pytest.ini`, `test_*.py` | `pip install pytest pytest-cov` |
| **Jest** | JavaScript | `jest.config.js`, `*.test.js` | `npm install --save-dev jest` |
| **Mocha** | JavaScript | `mocha.opts`, `test/` | `npm install --save-dev mocha` |
| **JUnit** | Java | `pom.xml`, `build.gradle` | Built into Maven/Gradle |
| **Go Test** | Go | `*_test.go` | Built into Go |

> **Note**: AI will automatically detect the test framework used by the project

## 🚀 Usage

### Method 1: Use AI Assistant

```
"Run project tests"
"Execute all unit tests"
"Run tests and generate coverage report"
```

### Method 2: Run Commands Manually

**Python (Pytest):**

```bash
pytest                          # Run all tests
pytest --cov=.                  # Generate coverage
pytest tests/test_api.py        # Run specific file
pytest -k "test_login"          # Run matching tests
pytest -v                       # Verbose output
```

**JavaScript (Jest):**

```bash
npm test                        # Run all tests
npm test -- --coverage          # Generate coverage
npm test -- api.test.js         # Run specific file
npm test -- -t "login"          # Run matching tests
jest --watch                    # Watch mode
```

**JavaScript (Mocha):**

```bash
npm test                        # Run all tests
mocha test/                     # Specify directory
mocha test/**/*.test.js         # Use glob
mocha --reporter spec           # Specify reporter format
```

**Java (Maven):**

```bash
mvn test                        # Run all tests
mvn test -Dtest=ApiTest         # Run specific test class
mvn test -DfailIfNoTests=false  # Don't fail if no tests
```

**Go:**

```bash
go test ./...                   # Run tests in all packages
go test -v ./...                # Verbose output
go test -cover ./...            # Coverage
go test -run TestLogin          # Run specific test
```

## 🎯 Test Types

### Unit Tests

- ✅ Function/method level testing
- ✅ Isolated dependencies (Mock/Stub)
- ✅ Fast execution
- ✅ High coverage targets

### Integration Tests

- ✅ Multi-component interaction testing
- ✅ Database/API integration
- ✅ End-to-end flows
- ✅ Environment dependencies

### Performance Tests

- ✅ Response time testing
- ✅ Load testing
- ✅ Stress testing
- ✅ Benchmark testing

## 📊 Output Examples

**Pytest Output:**

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

**Jest Output:**

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

## ⚙️ Configuration

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

## 🔄 CI/CD Integration

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

## 🆘 FAQ

**Q: How to run only failed tests?**  
A:

- Pytest: `pytest --lf` (last failed)
- Jest: `jest --onlyFailures`

**Q: How to skip slow tests?**  
A:

- Pytest: Use marker `@pytest.mark.slow` then `pytest -m "not slow"`
- Jest: Use `test.skip()` or `--testPathIgnorePatterns`

**Q: How to run tests in parallel?**  
A:

- Pytest: `pip install pytest-xdist` then `pytest -n auto`
- Jest: Parallel by default, use `--maxWorkers=4` to adjust

**Q: What if test coverage is low?**  
A:

1. Identify uncovered code: Check HTML report
2. Write missing tests
3. Refactor complex functions to improve testability

**Q: What if tests run slowly?**  
A:

1. Use parallel execution
2. Mock external dependencies (database, API)
3. Separate fast and slow tests

## 🔗 Related Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Jest Documentation](https://jestjs.io/)
- [Mocha Documentation](https://mochajs.org/)
- [Testing Best Practices](https://martinfowler.com/testing/)
