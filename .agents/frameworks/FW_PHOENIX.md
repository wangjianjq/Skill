---
tags: ["backend", "elixir", "realtime"]
---
# Framework: Phoenix

## Schema: Framework Specification

- framework: Phoenix
- category: backend
- language: Elixir
- latest_supported_version: 1.7+
- rendering_engine: LiveView
- state_management: Ecto
- router: Phoenix Router
- build_tool: Mix

---

## Core Stack

- **Language**: Elixir.
- **Component**: LiveView.

## Golden Snippet

```elixir
defmodule HelloWeb.PageController do
  use HelloWeb, :controller

  def index(conn, _params) do
    text(conn, "Hello from Phoenix!")
  end
end
```
