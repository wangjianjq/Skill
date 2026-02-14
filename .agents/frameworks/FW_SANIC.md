---
tags: ["backend", "python", "async"]
---
# Framework: Sanic

## Schema: Framework Specification

- framework: Sanic
- category: backend
- language: Python
- latest_supported_version: 23.x
- rendering_engine: N/A
- state_management: N/A
- router: Sanic Router
- build_tool: uv | poetry

---

## Core Stack

- **Speed**: Fast HTTP Server.

## Golden Snippet

```python
from sanic import Sanic, response

app = Sanic("MyHelloWorldApp")

@app.route("/")
async def test(request):
    return response.json({"hello": "world"})
```
