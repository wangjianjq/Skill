---
tags: ["web", "vue", "fullstack"]
---
# Framework: Nuxt

## Schema: Framework Specification

- framework: Nuxt
- category: web
- language: TypeScript/JavaScript
- latest_supported_version: 3.10+
- rendering_engine: Nitro
- state_management: Pinia
- router: Nuxt Router (auto-routing)
- build_tool: Vite

---

## [Modern] (v3.10+, Nitro)

- **Version**: Nuxt 3 (Nitro engine).
- **Patterns**: Composition API, Auto-imports, `useFetch`.
- **CSS**: Modern utilities (Tailwind/UnoCSS).

### Modern Snippet

```vue
<script setup>
const { data } = await useFetch('/api/v1/status')
</script>
```

## [Legacy] (v2.x)

- **Patterns**: Options API. `asyncData` and `fetch` hooks. `nuxt-link`.
