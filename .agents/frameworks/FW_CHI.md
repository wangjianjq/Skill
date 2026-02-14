---
tags: ["backend", "go", "std-compat"]
---
# Framework: Chi

## Schema: Framework Specification

- framework: Chi
- category: backend
- language: Go
- latest_supported_version: 5.x
- rendering_engine: N/A
- state_management: N/A
- router: Chi Router
- build_tool: go build

---

## Core Stack

- **Philosophy**: Lightweight, idiomatic.

## Golden Snippet

```go
import "github.com/go-chi/chi/v5"

func main() {
    r := chi.NewRouter()
    r.Get("/", func(w http.ResponseWriter, r *http.Request) {
        w.Write([]byte("welcome"))
    })
    http.ListenAndServe(":3000", r)
}
```
