---
tags: ["web", "vue", "frontend"]
---
# Framework: Vue

## Schema: Framework Specification

- framework: Vue (Vite)
- category: web
- language: TypeScript/JavaScript
- latest_supported_version: 3.5+
- rendering_engine: Vue Compiler
- state_management: Pinia
- router: Vue Router
- build_tool: Vite

---

## [Modern] (v3.4+, Vite)

- **Vue**: v3.4+ (SFC, `<script setup>`).
- **State**: Pinia.
- **Optimization**: Define models with `defineModel()`.

### Modern Snippet

```vue
<script setup>
const model = defineModel()
</script>
```

## [Legacy] (v2.x / v3 Early)

- **Vue**: v2.x (Options API).
- **State**: Vuex.
- **Patterns**: `data()`, `methods`, `computed` properties.
