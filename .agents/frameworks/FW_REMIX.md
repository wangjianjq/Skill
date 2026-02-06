---
tags: ["frontend", "react", "fullstack"]
---
# Framework: Remix (React Router v7)

## Schema: Framework Specification

- framework: Remix
- category: web
- language: TypeScript/JavaScript
- latest_supported_version: 2.x (React Router v7)
- rendering_engine: React Server Components
- state_management: React Context/Zustand
- router: React Router v7
- build_tool: Vite

---

## Core Stack

- **Loaders**: `loader` for data.
- **Actions**: `action` for mutations.

## Golden Snippet

```tsx
import { json } from "@remix-run/node";
import { useLoaderData } from "@remix-run/react";

export async function loader() {
  return json({ message: "Hello" });
}

export default function App() {
  const data = useLoaderData<typeof loader>();
  return <h1>{data.message}</h1>;
}
```
