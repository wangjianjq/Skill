---
tags: ["go1.22", "microservices"]
---
# Language: Go

## Schema: Language Specification

- language: Go
- category: systems_programming_language
- latest_supported_version: 1.22+
- module_system: go.mod (standard)
- error_handling: explicit (errors.Is, errors.As)
- logging: log/slog (structured, Go 1.21+)
- concurrency: goroutines + channels
- context_propagation: context.Context (mandatory)

---

## Environment

- **Version**: Go 1.22+
- **Modules**: standard `go.mod`.

## Best Practices

1. **Error Handling**: Explicit check `if err != nil`. Use `errors.Is` and `errors.As` (Go 1.13+).
2. **Logging**: Use standard library `log/slog` for structured logging (Go 1.21+).
3. **Context**: Always propagate `context.Context` for cancellation and timeouts.
4. **Concurrency**: Use Goroutines and Channels. Avoid shared state.
