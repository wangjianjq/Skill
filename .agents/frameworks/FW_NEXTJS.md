---
tags: ["web", "react", "fullstack"]
---
# Framework: Next.js

## Schema: Framework Specification

- framework: Next.js
- category: web
- language: TypeScript/JavaScript
- latest_supported_version: 15+
- rendering_engine: React Server Components
- state_management: React Context/Zustand
- router: App Router
- build_tool: Turbopack

---

## [v15+] (Modern Standard)

- **Router**: App Router (`app/`) ONLY. No `pages/`.
- **Data Fetching**: Server Components (`async function Page()`).
- **Mutations**: Server Actions (`'use server'`).
- **Caching**: Caching is **opt-in** by default.

### Modern Golden Snippet: Server Action

```tsx
'use server'
import { revalidatePath } from 'next/cache'

export async function createTodo(formData: FormData) {
  // Database logic here
  revalidatePath('/')
}
```

## [v12 - v14] (Stable/Legacy)

- **Router**: Pages Router (`pages/` directory).
- **Data Fetching**: `getStaticProps`, `getServerSideProps`.
- **Mutations**: API Routes (`pages/api/`).
- **Patterns**: HOCs, `useEffect` fetching (if no SSR).

### Legacy Golden Snippet: API Route

```ts
// pages/api/item.ts
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json({ name: 'Old School' })
}
```
