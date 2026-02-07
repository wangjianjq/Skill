---
tags: ["mobile", "harmonyos", "typescript-based"]
---
# Language: ArkTS (HarmonyOS)

## Schema: Language Specification

- language: ArkTS
- category: mobile_programming_language
- platform: HarmonyOS
- based_on: TypeScript
- latest_supported_version: HarmonyOS 6 (API 21)
- compiler: ArkCompiler (AOT)
- runtime: HongMeng Kernel (100% AOSP-free)
- type_system: strict (mandatory)
- concurrency: async/await + TaskPool
- api_version: API 21+
- logging_module: hilog

---

## [Modern] (HarmonyOS 6 / HarmonyOS Next 5.0+)

> **Latest**: HarmonyOS 6 (Released Oct 2025) is the current stable version

- **Compiler**: ArkCompiler with Ahead-of-Time (AOT) compilation for faster startup
- **Type System**: Strict typing MANDATORY, `any` type FORBIDDEN in production
- **Runtime**: HongMeng Kernel (Pure native, **100% AOSP-free** since HarmonyOS 6)
- **Concurrency**: Async/Await + Promises (recommended), TaskPool for multi-threading
- **Memory**: Automatic garbage collection with enhanced efficiency
- **API Version**: API 21 (HarmonyOS 6.0)

### HarmonyOS 6 Enhancements

- **Performance Gains** (vs HarmonyOS 5):
  - Content loading: **30% faster**
  - App startup: **11% faster**
  - Page rendering: **21% faster**
  - Overall fluidity: **15% improvement** (40% vs HarmonyOS 4)
  - Battery life: **+35-51 minutes**
- **AI Integration**: PanGu 5.5 AI models for intelligent features
  - Device-side Q&A model
  - Intelligent data retrieval C APIs (vectorization, knowledge Q&A)
  - AI Help Writing Assistant
- **Security**: StarShield Security Architecture
  - AI-driven protection (kernel to cloud)
  - Family Anti-Fraud, AI Anti-Fraud (deep-fake detection)
  - Anti-Peek Protection, Encrypted Sharing

### Core Language Features

- **Decorators**: Built-in decorators for UI and state management
  - `@Component`, `@Entry`, `@State`, `@Prop`, `@Link`
  - `@Provide`, `@Consume` (for cross-level state)
  - `@ObservedV2`, `@Trace` (State Management V2)
- **Type Safety**: Null safety enforced (similar to TypeScript strict mode)
- **Module System**: ESNext modules with HarmonyOS extensions

### Modern Snippet: ArkTS Component

```typescript
import { router } from '@kit.ArkUI';

@Entry
@Component
struct HomePage {
  @State counter: number = 0;
  
  build() {
    Column({ space: 16 }) {
      Text(`Counter: ${this.counter}`)
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
      
      Button('Increment')
        .onClick(() => {
          this.counter++;
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

### Best Practices (HarmonyOS 6)

- **NO `any` type**: Use generics or union types instead
- **Use `const/let`**: NEVER use `var`
- **State Management V2**: Prefer `@ObservedV2` + `@Trace` for complex objects
- **Async/Await**: For all asynchronous operations (network, file I/O)
- **TaskPool**: For CPU-intensive tasks to avoid UI blocking
- **Structured Logging**: Use `hilog` module (FORBIDDEN: `console.log` in production)
- **AI-First Development**: Leverage PanGu AI APIs for intelligent features
- **Security-First**: Implement StarShield best practices (encrypted sharing, anti-fraud)
- **Performance Budget**: Utilize Ark Engine optimizations for 60+ FPS UI
- **EROFS File System**: For system partitions (higher compression, better performance)

### Logging Standard

```typescript
import hilog from '@ohos.hilog';

// Correct ✅
hilog.info(0x0000, 'MyApp', 'User logged in: %{public}s', username);

// FORBIDDEN ❌
console.log('User logged in:', username);
```

## [Legacy] (HarmonyOS 2.x/3.x)

- **Language**: eTS (Extended TypeScript) or Java API compatibility
- **Runtime**: Multi-kernel system with OpenHarmony compatibility layer
- **UI Framework**: May use FAAbility model or XML-based layouts
- **Concurrency**: RxJS-based or callback patterns

### Legacy Note

**WARNING**: HarmonyOS 2.x/3.x shares architecture with Android compatibility layer.
For new projects, ALWAYS target HarmonyOS Next 5.0+ for pure native development.

---

## 🚨 Critical Rules

1. **Strict Typing**: `tsconfig.json` must have `"strict": true`
2. **No Console Logs**: Replace all `console.*` with `hilog` before production
3. **Lifecycle Awareness**: Always implement proper cleanup in `aboutToDisappear()`
4. **Performance**: Use `LazyForEach` for lists with 50+ items
5. **i18n Ready**: Use `$r('app.string.xxx')` for all UI strings (NO hardcoded text)
