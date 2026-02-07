---
tags: ["backend", "go", "micro"]
---
# Framework: Gin

## Schema: Framework Specification

- framework: Gin
- category: backend
- language: Go
- latest_supported_version: 1.10+
- rendering_engine: HTML/Template (optional)
- state_management: N/A
- router: Gin Router (Radix tree)
- build_tool: go build

---

## Core Stack

- **Router**: Radix tree.
- **Logging**: Integrate with `log/slog` via custom middleware for structured logs.

## Golden Snippet

```go
import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{"message": "pong"})
    })
    r.Run()
}
```
