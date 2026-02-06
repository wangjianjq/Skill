---
tags: ["backend", "node", "minimal"]
---
# Framework: Koa

## Schema: Framework Specification

- framework: Koa
- category: backend
- language: TypeScript/JavaScript
- latest_supported_version: 2.x
- rendering_engine: N/A
- state_management: N/A
- router: @koa/router
- build_tool: npm/pnpm/yarn

---

## Core Stack

- **Async**: Built for async/await.
- **Middleware**: Onion model.

## Golden Snippet

```javascript
const Koa = require('koa');
const app = new Koa();

app.use(async ctx => {
  ctx.body = 'Hello World';
});
```
