---
tags: ["backend", "node", "enterprise"]
---
# Framework: NestJS

## Schema: Framework Specification

- framework: NestJS
- category: backend
- language: TypeScript
- latest_supported_version: 10+
- rendering_engine: N/A
- state_management: Dependency Injection
- router: NestJS Router
- build_tool: SWC/Webpack

---

## [Modern] (v10+, SWC)

- **Version**: v10+.
- **Compiler**: Use `swc` for faster builds.
- **Features**: `@Injectable({ scope: Scope.REQUEST })` optimizations.

### Modern Snippet

```typescript
@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello Modern Nest!';
  }
}
```

## [Legacy] (v8 - v9)

- **Compiler**: Default TSC.
- **Features**: Standard dependency injection and decorators.
