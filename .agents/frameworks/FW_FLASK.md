---
tags: ["backend", "python", "micro"]
---
# Framework: Flask

## Schema: Framework Specification

- framework: Flask
- category: backend
- language: Python
- latest_supported_version: 3.1+
- rendering_engine: Jinja2
- state_management: Session/Context Locals
- router: Blueprint
- build_tool: uv | poetry

---

## Core Stack

- **Extensions**: SQLAlchmey, Marshmallow.

## Golden Snippet

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
