---
tags: ["backend", "node", "fullstack"]
---
# Framework: AdonisJS

## Schema: Framework Specification

- framework: AdonisJS
- category: backend
- language: TypeScript
- latest_supported_version: 6.x
- rendering_engine: Edge
- state_management: Lucid ORM
- router: Adonis Router
- build_tool: npm/yarn

---

## Core Stack

- **ORM**: Lucid.
- **Template**: Edge.

## Golden Snippet

```typescript
import router from '@adonisjs/core/services/router'

router.get('/', async () => {
  return { hello: 'world' }
})
```
