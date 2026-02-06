---
tags: ["embedded", "oop", "automotive"]
---
# Language: C++ (Modern Embedded)

## Schema: Language Specification

- language: C++
- category: systems_programming_language
- standard: C++17 | C++20
- profile: embedded-friendly
- exceptions: disabled (-fno-exceptions)
- rtti: disabled (-fno-rtti)
- stl_usage: minimal (static_vector preferred)
- memory_management: RAII + placement new

---

## Standards

- **Version**: C++17 or C++20.
- **Profile**: Embedded-friendly profile.
  - **NO Exceptions**: Compile with `-fno-exceptions`.
  - **NO RTTI**: Compile with `-fno-rtti`.
  - **NO STL**: Use `static_vector` or similar if full STL is too heavy.

## Best Practices

1. **RAII**: Use Resource Acquisition Is Initialization for hardware locks and buffers.
2. **Templates**: Prefer `constexpr` and templates over macros for type-safe hardware abstraction.
3. **Inlining**: Use `inline` for small getter/setter functions to avoid call overhead.
4. **Memory**: Prefer `std::array` over C-style arrays for bounds checking (if toolchain supports it).
5. **Placement New**: Use placement new if you must construct objects in pre-allocated memory buffers.
