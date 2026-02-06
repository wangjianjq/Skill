---
tags: ["prototyping", "hobbyist", "c++"]
---
# Framework: Arduino

## Schema: Framework Specification

- framework: Arduino
- category: embedded
- language: C/C++
- latest_supported_version: 2.x IDE + Boards Manager
- rendering_engine: N/A
- state_management: Global Variables/Static
- router: N/A
- build_tool: Arduino CLI | PlatformIO

---

## Best Practices

1. **Non-Blocking**: Avoid `delay()`. Use `millis()` based timers for all logic.
2. **Libraries**: Limit global scope. Encapsulate logic in classes or namespaces.
3. **Static**: Use `static` for persistent state within `loop()` if not part of a class.
4. **Prototyping**: Ideal for quick validation. Migrate to ESP-IDF or Zephyr for production-grade security and power management.
5. **Serial**: Standardized for initial debugging (`Serial.begin(115200)`).
