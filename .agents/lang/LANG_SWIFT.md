# Language: Swift

## Schema: Language Specification

- language: Swift
- category: mobile_programming_language
- platform: iOS | macOS
- latest_supported_version: 6.0+
- concurrency: data isolation (strict concurrency)
- persistence_modern: SwiftData
- persistence_legacy: CoreData
- ui_framework: SwiftUI | UIKit

---

## [Modern] (v6+, Swift Data)

- **Swift**: 6.0.
- **Concurrency**: Data isolation, Strict concurrency by default.
- **Persistence**: SwiftData (replaces CoreData).

### Modern Snippet: SwiftData

```swift
@Model
class Item {
  var timestamp: Date
}
```

## [Stable/Legacy] (v5.0 - v5.10)

- **UI**: SwiftUI or UIKit.
- **Persistence**: CoreData.
- **Concurrency**: `DispatchQueue.main` or early `async/wait`.
