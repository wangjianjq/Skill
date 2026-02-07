---
tags: ["backend", "node", "performance"]
---
# Framework: Fastify

## Schema: Framework Specification

- framework: Fastify
- category: backend
- language: TypeScript/JavaScript
- latest_supported_version: 5.0+
- rendering_engine: N/A
- state_management: N/A
- router: Fastify Router
- build_tool: npm/pnpm/yarn

---

## [Modern] (v4.x - v5+, ESM)

- **Version**: v5.0 (ESM/Node 20+).
- **Patterns**: Native async/await. Type-safe schemas with `TypeBox` or `Zod`.
- **Logging**: `pino` (Integrated).

### Modern Snippet

```javascript
import Fastify from 'fastify'
const fastify = Fastify({ logger: true })

fastify.get('/', async () => ({ status: 'Modern' }))
```

## [Legacy] (v3.x, CJS)

- **Patterns**: `require()`. JSON Schema validator built-in.
