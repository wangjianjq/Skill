---
tags: ["backend", "csharp", "enterprise"]
---
# Framework: .NET (ASP.NET Core)

## Schema: Framework Specification

- framework: .NET (ASP.NET Core)
- category: backend
- language: C#
- latest_supported_version: .NET 9
- rendering_engine: Kestrel
- state_management: Dependency Injection
- router: ASP.NET Core Router
- build_tool: dotnet CLI

---

## Core Stack

- **Language**: C# 13 (.NET 9).
- **API Style**:
  - **Minimal APIs**: Recommended for microservices, high-performance endpoints, and small projects.
  - **Controllers**: Recommended for large enterprise applications with complex routing, filters, and extensive endpoint counts.

## Golden Snippet

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.Run();
```
