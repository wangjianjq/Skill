# Knowledge: Python Quality Assurance Standards

> **Tags**: `logging-patterns`, `pytest-fixtures`, `best-practices`
> **Related Skill**: `SKILL_DEBUGGING.md`

## 1. Production Logging Strategy

### 1.1 The Golden Rules

1. **Never use `print()`**: It is unbuffered, unclassified, and blocking.
2. **Module-Level Loggers**: Always instantiate loggers per module to preserve hierarchy.

    ```python
    import logging
    logger = logging.getLogger(__name__)  # Correct
    # logger = logging.getLogger()          # Wrong (Root logger)
    ```

3. **Centralized Configuration**: Configure `logging.basicConfig` or `dictConfig` **only once** at the application entry point (`main.py` or `__init__.py`). Libraries should **never** configure the root logger, only add a `NullHandler`.

### 1.2 Recommended Configuration (Production)

```python
import logging
import sys

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            # logging.FileHandler("app.log") # Optional
        ]
    )
```

### 1.3 Exception Handling

Always capture stack traces for errors.

```python
try:
    dangerous_op()
except ValueError:
    logger.error("Operation failed", exc_info=True) # or logger.exception(...)
```

---

## 2. Advanced Testing with Pytest

### 2.1 Project Structure

```text
project_root/
├── src/
│   └── myapp/
│       └── logic.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py       # Shared fixtures
│   ├── unit/             # Fast, mocked tests
│   │   └── test_logic.py
│   └── integration/      # Slow, real I/O tests
│       └── test_db.py
└── pyproject.toml
```

### 2.2 Fixture Best Practices

1. **Scope Appropriately**: Use `scope="session"` for expensive resources (DB connections) and `scope="function"` (default) for state isolation.
2. **Conftest**: Put widely used fixtures in `tests/conftest.py` for auto-discovery.
3. **Yield Fixtures**: Use `yield` for cleanup (teardown).

    ```python
    @pytest.fixture
    def database():
        db = connect()
        yield db
        db.disconnect()
    ```

### 2.3 Parametrization

Avoid duplicating test logic. Use `@pytest.mark.parametrize`.

```python
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (10, 20)
])
def test_double(input, expected):
    assert double(input) == expected
```

### 2.4 Markers

Tag tests to run selective subsets (e.g., skip slow tests during dev).

- Mark: `@pytest.mark.slow`
- Run: `pytest -m "not slow"`

---

## 3. Integration Strategy

1. **Do not mock** in integration tests.
2. **Separate Runs**: Run unit tests on every commit; run integration tests before merge.
3. **Temp Logging for AI**: When asking LLMs to debug tests, instruct them to enable `DEBUG` level logging to a temporary file (`debug_test.log`) to capture internal state without cluttering stdout.

---

## 4. Node.js & TypeScript QA

### 4.1 Logging (Pino)

- **Library**: Use `pino` for high-performance JSON logging.
- **Best Practice**:
  - **No Console**: Avoid `console.log` in production.
  - **Async Logging**: Enable `pino.destination({ sync: false })` for high throughput.
  - **Redaction**: Configure `redact` for sensitive keys (e.g., `["req.headers.authorization"]`).

### 4.2 Testing (Jest/Vitest)

- **Framework**: `jest` (standard) or `vitest` (if using Vite).
- **Structure**: Co-locate tests `feature.test.ts` next to `feature.ts` OR usage a top-level `__tests__` folder.
- **Pattern**:

    ```typescript
    describe("UserService", () => {
        it("should create user", async () => {
             // Arrange, Act, Assert
             expect(result).toBeDefined();
        });
    });
    ```

---

## 5. Go QA Standards

### 5.1 Logging (Slog)

- **Library**: Standard library `log/slog` (Go 1.21+).
- **Format**: JSON for production.

    ```go
    logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
    logger.Info("processed request", "id", reqID, "status", 200)
    ```

- **Context**: Always pass `ctx` to loggers if using custom handlers for tracing.

### 5.2 Testing

- **Library**: Standard `testing` package + `testify/assert` for ergonomics.
- **Table-Driven Tests**: The Go Standard.

    ```go
    func TestAdd(t *testing.T) {
        tests := []struct {
            name string
            a, b int
            want int
        }{
            {"positive", 1, 2, 3},
        }
        for _, tt := range tests {
            t.Run(tt.name, func(t *testing.T) {
                if got := Add(tt.a, tt.b); got != tt.want {
                    t.Errorf("Add() = %v, want %v", got, tt.want)
                }
            })
        }
    }
    ```

---

## 6. C++ QA Standards

### 6.1 Logging (Spdlog)

- **Library**: `spdlog` (Fast, header-only).
- **Pattern**:

    ```cpp
    #include "spdlog/spdlog.h"
    spdlog::info("Welcome to spdlog!");
    spdlog::error("Some error message with arg: {}", 1);
    ```

### 6.2 Testing (GoogleTest)

- **Library**: GoogleTest (`gtest`).
- **Structure**:

    ```cpp
    TEST(MathTest, AddsTwoOnes) {
        EXPECT_EQ(add(1, 1), 2);
    }
    ```

---

## 7. Frontend (React/Vue)

### 7.1 Testing Strategy

- **Library**: React Testing Library + Vitest.
- **Philosophy**: "Test behaviors, not implementation details."
- **Selectors**:
  - **Preferred**: `getByRole`, `getByLabelText`, `getByText` (Accessible).
  - **Avoid**: `getByTestId` (unless necessary), CSS selectors.
- **User Events**: Always use `user-event` over `fireEvent`.

    ```javascript
    ```javascript
    await user.click(screen.getByRole('button', { name: /submit/i }))
    ```

---

## 8. Java & Kotlin (JVM) QA

### 8.1 Logging (SLF4J)

- **Library**: Use SLF4J as a facade with Logback as the implementation.
- **Best Practice**:
  - **Parameterized Logging**: Use placeholders `{}` to avoid string concatenation overhead.

    ```java
    logger.info("User {} performed action {}", userId, action);
    ```

  - **Context**: Use MDC (Mapped Diagnostic Context) to track request IDs across threads.

### 8.2 Testing (JUnit 5)

- **Framework**: JUnit 5 + AssertJ (for fluent assertions).
- **Mocking**: Mockito for isolating components.

---

## 9. Mobile QA (Android & iOS)

### 9.1 Android Logging (Timber)

- **Library**: Use `Timber` ( Jake Wharton's logging utility).
- **Best Practice**:
  - **Debug Only Trees**: Plant `DebugTree` only in internal builds.

    ```kotlin
    if (BuildConfig.DEBUG) Timber.plant(Timber.DebugTree())
    ```

  - **Automatic Tags**: Timber uses the class name as the tag automatically.

### 9.2 iOS Logging (OSLog)

- **Library**: Use Apple's Unified Logging (`os_log` or `Logger` in Swift).
- **Privacy**: Use `.private` or `.sensitive` for user data to ensure it is redacted in production logs.

    ```swift
    import OSLog
    let logger = Logger(subsystem: "com.myapp", category: "Auth")
    logger.log("User \(username, privacy: .private) logged in")
    ```

### 9.3 Mobile Testing

- **Unit**: XCTest (iOS), JUnit (Android).
- **UI**: XCUITest (iOS), Espresso or Compose Test (Android).
- **Rule**: Keep UI tests minimal; focus on "Critical Path" and rely on Unit tests for logic.

---

## 10. C# / .NET QA

### 10.1 Logging

- **Framework**: `Microsoft.Extensions.Logging`.
- **Best Practice**: Use **Structured Logging** with Message Templates.

    ```csharp
    _logger.LogInformation("Processed {count} items for user {userId}", count, userId);
    ```

### 10.2 Testing (xUnit)

- **Framework**: `xUnit` + `FluentAssertions`.
- **Pattern**: Use `ITestOutputHelper` for log capture in tests.

---

## 11. Rust & Zig QA

### 11.1 Rust (Tracing)

- **Logging**: Use the `tracing` crate for spans and events.
- **Testing**: `cargo test`. Use `test-log` crate to automatically capture logs during failure.

### 11.2 Zig

- **Logging**: `std.log`. Use `scope` to filter logs by module.
- **Testing**: `std.testing`. Zig co-locates tests in the same file.

    ```zig
    test "logic test" {
        try std.testing.expect(add(1, 1) == 2);
    }
    ```

---

## 12. Embedded & Hardware QA (Specialized)

### 12.1 Logging (Resource Constrained)

- **Frameworks**: `ESP_LOG` (ESP-IDF), `SEGGER_RTT` (Hard Real-time), `printk` (Zephyr).
- **Rule**: Use pre-processor guards to strip `DEBUG` logs from production binary to save flash.

### 12.2 Hardware-in-the-Loop (HIL)

- **Strategy**:
    1. **Host-side Unit Tests**: Compile logic on X86 with mocks for hardware peripherals.
    2. **Instrumented Verification**: Use `SKILL_INSTRUMENT_*` (Saleae, DMM) to verify physical signals (I2C/SPI timing) against expected protocol patterns.
    3. **Assertion**: Use J-Link RTT to assert internal state while the device is running physical cycles.
