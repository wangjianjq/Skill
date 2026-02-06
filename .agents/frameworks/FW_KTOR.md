---
tags: ["backend", "kotlin", "async"]
---
# Framework: Ktor

## Schema: Framework Specification

- framework: Ktor
- category: backend
- language: Kotlin
- latest_supported_version: 3.x
- rendering_engine: N/A
- state_management: N/A
- router: Ktor Routing
- build_tool: Gradle/Maven

---

## Core Stack

- **Language**: Kotlin.
- **Server**: Netty / CIO.

## Golden Snippet

```kotlin
import io.ktor.server.application.*
import io.ktor.server.response.*
import io.ktor.server.routing.*

fun Application.module() {
    routing {
        get("/") {
            call.respondText("Hello World!")
        }
    }
}
```
