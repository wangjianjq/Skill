---
tags: ["csharp", "dotnet", "linq"]
---
# Language: C# (Modern)

## Schema: Language Specification

- language: C#
- category: general_purpose_language
- latest_supported_version: C# 13 (.NET 9)
- nullable: enabled
- modern_features: params collections | performance LINQ | field-backed properties
- async_pattern: Task + ValueTask
- data_structures: records (immutable DTOs)
- pattern_matching: switch expressions

---

## 1. Versioning

- **Target**: C# 13 (.NET 9).
- **Nullable**: Enabled.
- **New in .NET 9**: `params` collections (array, list, span), performance-optimized LINQ (`CountBy`, `AggregateBy`), and field-backed properties (preview).

## 2. Best Practices

- **Async/Await**: Use `Task` and `ValueTask` everywhere. Avoid `.Result` or `.Wait()` (Deadlock risk).
- **LINQ**: Prefer LINQ for data manipulation, but be aware of deferred execution.
- **Records**: Use `record` types for immutable DTOs.
- **Pattern Matching**: Use extensive switch expressions.

## 3. Golden Snippet

```csharp
public record User(int Id, string Name);

public async Task<User?> GetUserAsync(int id)
{
    // Minimal API style dependency injection & logging assumed
    return await db.Users.FindAsync(id);
}
```
