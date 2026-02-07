---
tags: ["rtos", "kernel", "multitasking"]
---
# Framework: FreeRTOS

## Schema: Framework Specification

- framework: FreeRTOS
- category: embedded
- language: C
- latest_supported_version: 11.x
- rendering_engine: N/A
- state_management: Task/Queue/Semaphore
- router: N/A
- build_tool: CMake | Makefile

---

## Core Concepts

- **Scheduler**: Preemptive, deterministic multitasking.
- **Config**: `FreeRTOSConfig.h` defines kernel behavior.

## Best Practices

1. **Task Priority**: Keep the IDLE task priority at 0. Assign higher priorities to time-critical drivers.
2. **Synchronization**: Use Semaphores/Mutexes for resource sharing. Use Direct-to-Task Notifications (v10.x+) for faster, lower-overhead signaling.
3. **Heap**: Select the appropriate heap manager (`heap_4.c` is the general recommendation).
4. **ISRs**: ONLY use `FromISR` suffixed APIs inside interrupt handlers.
5. **Stack Overflow**: Enable `configCHECK_FOR_STACK_OVERFLOW` during debugging.
