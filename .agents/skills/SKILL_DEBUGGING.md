# Skill: Debugging & Testing Standards

> **Skill ID**: `SKILL_DEBUGGING`
> **Tags**: `debug-rules`, `logging`, `testing`, `polyglot-qa`
> **Version**: 1.2
> **Related Knowledge**: `KNOWLEDGE_QA.md`

## 1. Logging Standards

**Rationale**: `print()` or `console.log()` statements are often unbuffered, unclassified, and hard to filter. Structured logging provides timestamps, levels, and output control.

### Rules

- **MUST**: Use the standard logging framework for the current stack (see `KNOWLEDGE_QA.md`).
- **MUST**: Use a standard formatter that includes `[TIMESTAMP][LEVEL][LOGGER_NAME]`.
- **FORBIDDEN**: Do NOT use raw print/console statements for production output.

### Levels (Standard Mapping)

- `DEBUG`: Detailed diagnostic info.
- `INFO`: Confirmation of working execution.
- `WARNING`: Unexpected events, but app still running.
- `ERROR`: Functionality or transaction failed.
- `CRITICAL/FATAL`: App crash imminent or data corruption.

## 2. Exception & Error Handling

**Rationale**: Silent failures or broad catches hide bugs and make root-cause analysis impossible.

### Rules

- **MUST**: Catch specific exceptions/errors.
- **FORBIDDEN**: "Empty" catch blocks (e.g., `except: pass` or `catch(e){}`).
- **MUST**: Include the full error context and stack trace (if available) when logging Errors.

## 3. Testing Standards

**Rationale**: Tests ensure reliability and prevent regressions across different language stacks.

### Rules

- **Framework**: Use the stack's standard runner (e.g., `pytest`, `jest`, `testing`, `google-test`, `junit`, `XCTest`).
- **Location**: Store tests in a predictable structure (e.g., `tests/` directory or co-located `.test.` files).
- **Naming**: Follow the discovery convention of the chosen framework.
- **Styles**:
  - **Unit Tests**: Focus on logic; mock external dependencies.
  - **Integration Tests**: Verify real interactions between components/services.

## 4. Platform-Specific Debugging

- **Tkinter (Python)**: Trap `TclError` and redirect `stderr` to a log file.
- **Node.js**: Use `pino` for performance; redact sensitive keys.
- **Go**: Use `slog` for structured concurrency-safe logging.
- **Mobile**: Use `Timber` (Android) or `OSLog` (iOS) with proper privacy redaction.

## 5. LLM-Assisted Testing Workflow

**Rationale**: Leverage AI to maintain high test coverage with minimal friction.

### Feature Completion Protocol

**Trigger**: When the Agent finishes implementing a single feature/function.

1. **Ask**: "Should I write a unit test for this feature?"
2. **Action**: If User says **YES**:
    - Build a test file using the appropriate stack framework.
    - **Temp Logging**: Enable maximum verbosity (e.g., `DEBUG` level) outputting to a temporary file (`debug_test.log`) during the test run to capture internal state.
    - Run the test and report results.
    - Ask if the temp logging file should be kept.

### Batch Implementation Protocol

**Trigger**: When the Agent finishes a series of related features (a "Batch").

1. **Ask**: "Should I perform an Integration Test?"
2. **Action**: If User says **YES**:
    - Verify interaction between the newly created/modified components.
    - Use the integration suite of the target stack.
    - Report verification results.
