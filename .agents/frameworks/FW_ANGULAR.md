---
tags: ["web", "angular", "fullstack"]
---
# Framework: Angular

## Schema: Framework Specification

- framework: Angular
- category: web
- language: TypeScript
- latest_supported_version: 17+
- rendering_engine: Angular Compiler (Ivy)
- state_management: Signals (v17+)
- router: Angular Router
- build_tool: esbuild + Vite

---

## [Modern] (v17+, Signals)

- **Version**: v17+ (Signals mandatory for new state).
- **Patterns**: Standalone components, `@if/@for` flow control.
- **Rendering**: SSR/Hydration by default.

### Modern Snippet

```typescript
@Component({
  standalone: true,
  template: `{{ count() }}`
})
export class App {
  count = signal(0);
}
```

## [Legacy] (v12 - v16, RxJS)

- **Patterns**: Declarative `NgModules`. Extensive use of RxJS observables.
- **Boilerplate**: Zone.js based change detection.
