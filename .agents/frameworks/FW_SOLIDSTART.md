---
tags: ["frontend", "solid", "fullstack"]
---
# Framework: SolidStart

## Schema: Framework Specification

- framework: SolidStart
- category: web
- language: TypeScript/JavaScript
- latest_supported_version: 1.0+
- rendering_engine: SolidJS
- state_management: Signals (fine-grained reactivity)
- router: SolidStart Router
- build_tool: Vite

---

## Core Stack

- **Signals**: Fine-grained reactivity.
- **SSR**: Enabled.

## Golden Snippet

```tsx
import { createSignal } from "solid-js";

export default function Counter() {
  const [count, setCount] = createSignal(0);
  return <button onClick={() => setCount(c => c + 1)}>{count()}</button>;
}
```
