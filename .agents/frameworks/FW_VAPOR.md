---
tags: ["backend", "swift", "server-side-swift"]
---
# Framework: Vapor

## Schema: Framework Specification

- framework: Vapor
- category: backend
- language: Swift
- latest_supported_version: 4.x
- rendering_engine: Leaf
- state_management: Fluent ORM
- router: Vapor Router
- build_tool: Swift Package Manager

---

## Core Stack

- **Language**: Swift.
- **Async**: Swift Concurrency.

## Golden Snippet

```swift
import Vapor

func routes(_ app: Application) throws {
    app.get { req in
        return "It works!"
    }
}
```
