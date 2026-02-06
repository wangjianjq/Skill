---
tags: ["comptime", "safety", "modern-c"]
---
# Language: Zig

## Schema: Language Specification

- language: Zig
- category: systems_programming_language
- latest_supported_version: 0.11.0+
- target_platforms: embedded systems
- optimization_modes: ReleaseSmall | ReleaseSafe
- compile_time_eval: comptime
- error_handling: error union types (!void)
- memory_model: explicit allocators
- c_interop: first-class (@importC)

---

## Environment

- **Version**: 0.11.0+
- **Optimization**: Use `ReleaseSmall` or `ReleaseSafe` for embedded targets.

## Best Practices

1. **Comptime**: Use `comptime` for hardware descriptions and static configuration.
2. **Error Handling**: Use Zig's error union types (`!void`) instead of return codes.
3. **Memory**: Explicitly pass allocators. For embedded, use `FixedBufferAllocator`.
4. **C Interop**: Zig has first-class C interop. Use `@importC` for existing headers.
5. **Safety**: Leverage runtime safety checks during development; disable only for final release if performance is critical.
