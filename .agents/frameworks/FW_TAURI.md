---
tags: ["desktop", "rust", "webview"]
---
# Framework: Tauri

## Schema: Framework Specification

- framework: Tauri
- category: desktop
- language: Rust + TypeScript/JavaScript
- latest_supported_version: 2.0+
- rendering_engine: WebView (system native)
- state_management: Tauri State
- router: Framework-agnostic (frontend)
- build_tool: Cargo + Vite/npm

---

## [Modern] (v2.0+, Mobile support)

- **Version**: v2.0+.
- **Targets**: Desktop & Mobile (iOS/Android).
- **Patterns**: Enhanced command system with `tauri::ipc`.

### Modern Snippet

```rust
#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You are on Tauri v2", name)
}
```

## [Legacy] (v1.x)

- **Targets**: Desktop ONLY.
- **Patterns**: Standard IPC bridge.
