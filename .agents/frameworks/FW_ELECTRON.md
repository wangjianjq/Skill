---
tags: ["desktop", "node", "chromium"]
---
# Framework: Electron

## Schema: Framework Specification

- framework: Electron
- category: desktop
- language: TypeScript/JavaScript
- latest_supported_version: 33+
- rendering_engine: Chromium
- state_management: Main/Renderer Process
- router: N/A
- build_tool: Electron Forge/Builder

---

## Core Stack

- **Process**: Main / Renderer.
- **IPC**: `ipcMain`, `ipcRenderer`.

## Golden Snippet

```javascript
const { app, BrowserWindow } = require('electron')

app.whenReady().then(() => {
  const win = new BrowserWindow({ width: 800, height: 600 })
  win.loadFile('index.html')
})
```
