---
tags: ["mobile", "react", "native"]
---
# Framework: React Native

## Schema: Framework Specification

- framework: React Native
- category: mobile
- language: TypeScript/JavaScript
- latest_supported_version: 0.76+
- rendering_engine: Fabric (New Architecture)
- state_management: React Context/Zustand
- router: React Navigation
- build_tool: Metro

---

## Core Stack

- **Engine**: Hermes (Default).
- **Architecture**:
  - **New Architecture (0.76+)**: Fabric (Rendering), TurboModules (Lazy loading), Bridgeless (Native JSI). Enabled by default.
  - **Legacy**: Bridge-based. Use only for incompatible libraries.
- **UI**: Framework-agnostic, but prefer `@shopify/flash-list` over `FlatList` for long lists.

## Versioning Guide

- **0.76+**: New Architecture is mandatory/default. Bridgeless is active.
- **<0.76**: Check `newArchEnabled` in `gradle.properties` or `Podfile`.

## Golden Snippet

```tsx
import { Text, View } from 'react-native';

export default function App() {
  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Text>Hello Native</Text>
    </View>
  );
}
```
