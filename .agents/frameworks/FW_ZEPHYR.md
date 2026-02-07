---
tags: ["rtos", "linux-like", "cross-platform"]
---
# Framework: Zephyr RTOS

## Schema: Framework Specification

- framework: Zephyr RTOS
- category: embedded
- language: C
- latest_supported_version: 3.x
- rendering_engine: N/A
- state_management: Kernel Objects
- router: N/A
- build_tool: West + CMake

---

## Core Configuration

- **Device Tree**: Use `.dts` and `.overlay` files for hardware descriptions.
- **Kconfig**: Configuration via `.conf` files (Menuconfig compatible).

## Best Practices

1. **Drivers**: Use the `device_get_binding` and `DEVICE_DT_GET` macros.
2. **Threads**: Prefer static thread definition using `K_THREAD_DEFINE`.
3. **Work Queues**: Use System Work Queues for non-urgent background tasks.
4. **Logging**: Use the structured `LOG_INF`, `LOG_ERR` macros indexed by module.
5. **Shell**: Enable the Zephyr Shell for runtime inspection via UART.
