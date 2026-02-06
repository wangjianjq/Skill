---
tags: ["backend", "python", "api"]
---
# Framework: FastAPI

## Schema: Framework Specification

- framework: FastAPI
- category: backend
- language: Python
- latest_supported_version: 0.115+
- rendering_engine: N/A
- state_management: Dependency Injection
- router: APIRouter
- build_tool: uv | poetry

---

## [Modern] (Pydantic v2+, Python 3.10+)

- **Validation**: Pydantic v2 (Rust-based).
- **Patterns**: Annotated dependencies (`Annotated[str, Depends(...)]`).

### Modern Snippet

```python
from typing import Annotated
from fastapi import Depends, FastAPI

@app.get("/")
def read_root(q: Annotated[str | None, Query()] = None):
    return {"q": q}
```

## [Legacy] (Pydantic v1)

- **Validation**: Pydantic v1.
- **Typing**: Use `typing.List`, `typing.Dict`.
