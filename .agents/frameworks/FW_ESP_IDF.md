---
tags: ["esp32", "freertos", "iot"]
---
# Framework: ESP-IDF (Espressif IoT Development Framework)

## Schema: Framework Specification

- framework: ESP-IDF
- category: embedded
- language: C
- latest_supported_version: 5.x
- rendering_engine: N/A
- state_management: FreeRTOS Tasks
- router: N/A
- build_tool: CMake + idf.py

---

## Core Configuration

- **Version**: v5.x (Modern Standard).
- **Build System**: CMake.
- **Menuconfig**: Use `sdkconfig` for hardware-specific configurations.

## Best Practices

1. **Event Loop**: Use the default event loop for Wi-Fi and IP events.
2. **Tasks**: Always define task stack sizes carefully. Use `xTaskCreatePinnedToCore` for dual-core synchronization.
3. **Storage**: Use NVS (Non-Volatile Storage) for small key-value pairs, LittleFS/SPIFFS for larger files.
4. **Logging**: Use `ESP_LOGI`, `ESP_LOGE`, etc. Set log level via menuconfig or `esp_log_level_set`.
5. **Error Handling**: Wrap SDK calls with `ESP_ERROR_CHECK()` during development to catch initialization failures early.
