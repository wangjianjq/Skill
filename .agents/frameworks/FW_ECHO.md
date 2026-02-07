---
tags: ["backend", "go", "performance"]
---
# Framework: Echo

## Schema: Framework Specification

- framework: Echo
- category: backend
- language: Go
- latest_supported_version: 4.x
- rendering_engine: N/A
- state_management: N/A
- router: Echo Router
- build_tool: go build

---

## Core Stack

- **Context**: Centralized context object.

## Golden Snippet

```go
import "github.com/labstack/echo/v4"

func main() {
    e := echo.New()
    e.GET("/", func(c echo.Context) error {
        return c.String(http.StatusOK, "Hello, World!")
    })
    e.Start(":1323")
}
```
