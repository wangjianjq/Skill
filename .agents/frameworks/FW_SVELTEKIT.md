---
tags: ["web", "svelte", "fullstack"]
---
# Framework: SvelteKit

## Schema: Framework Specification

- framework: SvelteKit
- category: web
- language: TypeScript/JavaScript
- latest_supported_version: 2+
- rendering_engine: Svelte 5 Compiler
- state_management: Svelte Runes ($state, $derived)
- router: SvelteKit Router (file-based)
- build_tool: Vite

---

## [Modern] (v2+, Svelte 5 Runes)

- **Version**: SvelteKit 2 (Svelte 5 Runes).
- **Patterns**: Use `$state`, `$derived`, `$effect`.
- **Routing**: Directory-based routing with `+page.svelte`.

### Modern Snippet

```svelte
<script>
  let count = $state(0);
</script>
<button onclick={() => count++}>{count}</button>
```

## [Legacy] (Svelte 4)

- **Patterns**: `let count = 0;` with `$:` reactive statements.
- **Event Handling**: `on:click`.
