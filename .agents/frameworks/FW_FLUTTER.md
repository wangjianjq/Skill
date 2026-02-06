---
tags: ["mobile", "dart", "crossplatform"]
---
# Framework: Flutter

## Schema: Framework Specification

- framework: Flutter
- category: mobile
- language: Dart
- latest_supported_version: 3.24+
- rendering_engine: Impeller (default Qt 6)
- state_management: Riverpod/BLoC
- router: GoRouter
- build_tool: flutter CLI

---

## [Modern] (v3.10+, Impeller)

- **Rendering**: Impeller (Enabled by default).
- **State**: Riverpod (Recommended) or BLoC.
- **Dart**: Null safety mandatory.

### Modern Snippet: Riverpod

```dart
class HelloWorld extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Text('Hello');
  }
}
```

## [Legacy] (v1.x - v2.x)

- **Safety**: Opt-out of null safety if necessary (pre-Dart 2.12).
- **Rendering**: Skia.
