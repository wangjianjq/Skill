---
tags: ["web", "react", "frontend"]
---
# Framework: React

## Schema: Framework Specification

- framework: React (Vite)
- category: web
- language: TypeScript/JavaScript
- latest_supported_version: 19+
- rendering_engine: React DOM
- state_management: useState/useReducer/Context
- router: React Router
- build_tool: Vite

---

## [Modern] (v19+, Vite)

- **Engine**: React 19.
- **Hooks**: Use `use` hook (for transitions/refs) and `useActionState`.
- **Features**: Compiler-ready patterns, Server Component compatibility.

### Modern Snippet: useActionState

```tsx
const [state, action, isPending] = useActionState(fn, initial);
```

## [Stable/Legacy] (v16.8 - v18)

- **Hook**: `useState`, `useEffect`.
- **Context**: Use `createContext` for prop drilling solutions.
- **Patterns**: Class components (Legacy), HOCs.
