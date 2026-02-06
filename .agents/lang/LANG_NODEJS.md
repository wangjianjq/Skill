---
tags: ["node20", "typescript", "npm"]
---
# Language: Node.js / TypeScript

## Schema: Language Specification

- language:Node.js + TypeScript
- category: backend_programming_language
- runtime: Node.js v20 (LTS) | v22
- typescript_version: 5.4+ (Strict Mode)
- package_manager: pnpm (preferred)
- module_system: ESM (type: module)
- async_pattern: async/await (exclusive)
- validation: Zod
- testing: Vitest

---

## Environment

- **Runtime**: Node.js v20 (LTS) or v22.
- **Language**: TypeScript 5.4+ (Strict Mode).
- **Manager**: `pnpm` (Fastest, disk efficient).

## Best Practices

1. **Modules**: ESM Only (`"type": "module"` in package.json).
2. **Async**: `async/await` exclusively. No callbacks.
3. **Validation**: `Zod` for runtime validation.
4. **Testing**: `Vitest` (preferred over Jest).
