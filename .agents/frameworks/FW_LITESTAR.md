---
tags: ["backend", "python", "performance"]
---
# Framework: Litestar

## Schema: Framework Specification

- framework: Litestar
- category: backend
- language: Python
- latest_supported_version: 2.x
- rendering_engine: N/A
- state_management: Dependency Injection
- router: Litestar Router
- build_tool: uv | poetry

---

## Core Stack

- **Type-safe**: Built on Modern Python.
- **Di**: Powerful Dependency Injection.

## Golden Snippet

```python
from litestar import Litestar, get

@get("/")
async def hello_world() -> dict[str, str]:
    return {"hello": "world"}

app = Litestar(route_handlers=[hello_world])
```
