---
tags: ["backend", "node", "edge"]
---
# Framework: Hono

## Schema: Framework Specification

- framework: Hono
- category: backend
- language: TypeScript/JavaScript
- latest_supported_version: 4.x
- rendering_engine: N/A
- state_management: N/A
- router: Hono Router
- build_tool: Any (Node/Deno/Bun/CF Workers)

---

## Core Stack

- **Runtime**: Any (Node, Deno, Bun, Cloudflare).
- **Type**: Web Standards.

## Golden Snippet

```typescript
import { Hono } from 'hono'
const app = new Hono()

app.get('/', (c) => c.text('Hono!'))

export default app
```
