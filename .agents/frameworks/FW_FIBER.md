---
tags: ["backend", "go", "express-like"]
---
# Framework: Fiber

## Schema: Framework Specification

- framework: Fiber
- category: backend
- language: Go
- latest_supported_version: 3.x
- rendering_engine: N/A
- state_management: N/A
- router: Fiber Router
- build_tool: go build

---

## Core Stack

- **Engine**: Fasthttp.

## Golden Snippet

```go
import "github.com/gofiber/fiber/v2"

func main() {
    app := fiber.New()
    app.Get("/", func(c *fiber.Ctx) error {
        return c.SendString("Hello, World!")
    })
    app.Listen(":3000")
}
```
