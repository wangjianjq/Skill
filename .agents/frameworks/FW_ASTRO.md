---
tags: ["frontend", "mpa", "content"]
---
# Framework: Astro

## Schema: Framework Specification

- framework: Astro
- category: web
- language: TypeScript/JavaScript
- latest_supported_version: 4.x
- rendering_engine: Astro Compiler (Islands Architecture)
- state_management: Framework-agnostic
- router: File-based routing
- build_tool: Vite

---

## Core Stack

- **Islands**: Partial hydration (`client:load`).
- **Content**: Content Collections (`src/content`).

## Golden Snippet

```astro
---
const { title } = Astro.props;
---
<h1>{title}</h1>
```
