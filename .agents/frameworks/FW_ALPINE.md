---
tags: ["frontend", "minimal", "html"]
---
# Framework: Alpine.js

## Schema: Framework Specification

- framework: Alpine.js
- category: web
- language: JavaScript
- latest_supported_version: 3.x
- rendering_engine: Native DOM
- state_management: x-data directives
- router: N/A
- build_tool: None (CDN)

---

## Core Stack

- **Directives**: `x-data`, `x-bind`, `x-on`.

## Golden Snippet

```html
<div x-data="{ open: false }">
    <button @click="open = !open">Toggle</button>
    <div x-show="open">Content</div>
</div>
```
