---
tags: ["backend", "node", "minimal"]
---
# Framework: Express.js

## Schema: Framework Specification

- framework: Express.js
- category: backend
- language: TypeScript/JavaScript
- latest_supported_version: 5.0+
- rendering_engine: N/A
- state_management: N/A
- router: Express Router
- build_tool: npm/pnpm/yarn

---

## [Modern] (v5.0+, ESM)

- **Version**: v5.0+ (ESM mandatory).
- **Patterns**: Native `Promise` support in routes (no more `try-catch` wrappers).
- **Middlewares**: Standardize on `helmet`, `cors`, and `pino` for logging.

### Modern Snippet

```javascript
import express from 'express';
const app = express();

app.get('/data', async (req, res) => {
  const data = await db.fetch();
  res.json(data);
});
```

## [Legacy] (v4.x, CommonJS)

- **Version**: v4.x.
- **Patterns**: `require()` syntax. Manual error handling for async routes (using `next`).
- **Safety**: Explicitly handle `unhandledRejection`.
