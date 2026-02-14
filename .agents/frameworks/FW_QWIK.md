---
tags: ["frontend", "qwik", "resumable"]
---
# Framework: Qwik

## Schema: Framework Specification

- framework: Qwik
- category: web
- language: TypeScript/JavaScript
- latest_supported_version: 1.x
- rendering_engine: Qwik Optimizer (resumable)
- state_management: Signals
- router: Qwik City
- build_tool: Vite

---

## Core Stack

- **Resumability**: No hydration.
- **Signals**: `useSignal`.

## Golden Snippet

```tsx
import { component$, useSignal } from '@builder.io/qwik';

export default component$(() => {
  const count = useSignal(0);
  return <button onClick$={() => count.value++}>{count.value}</button>;
});
```
