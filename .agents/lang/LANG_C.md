---
tags: ["embedded", "drivers", "performance"]
---
# Language: C (Embedded Standard)

## Schema: Language Specification

- language: C
- category: systems_programming_language
- standard: C99 | C11
- safety_guidelines: MISRA-C:2012 | CERT C
- memory_model: static allocation (real-time)
- concurrency: volatile + ISR
- type_headers: stdint.h (fixed-width types)
- target_platforms: embedded systems

---

## Standards

- **Version**: C99 or C11. Avoid K&R C.
- **Safety**: Follow MISRA-C:2012 or CERT C guidelines where possible.
- **Headers**: Use `<stdint.h>` for fixed-width types (`uint8_t`, `int32_t`).

## Best Practices

1. **Memory Management**: STRICTLY NO dynamic memory allocation (`malloc`/`free`) in real-time loops. Use static allocation or stack-based pools.
2. **Concurrency**: Use `volatile` for variables modified in ISRs (Interrupt Service Routines).
3. **Hardware Access**: Use peripheral driver libraries (HAL/LL) instead of direct register manipulation unless performance is critical.
4. **Error Handling**: Functions should return error codes (`esp_err_t`, `int`). Check every return value.
5. **Formatting**: Use 4 spaces for indentation. Ensure Doxygen-style comments for public APIs.
