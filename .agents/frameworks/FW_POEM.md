---
tags: ["backend", "rust", "full-featured"]
---
# Framework: Poem

## Schema: Framework Specification

- framework: Poem
- category: backend
- language: Rust
- latest_supported_version: 3.x
- rendering_engine: N/A
- state_management: N/A
- router: Poem Router
- build_tool: Cargo

---

## Core Stack

- **Feature**: OpenAPI support builtin.

## Golden Snippet

```rust
use poem::{handler, Request, Route, Server};

#[handler]
fn hello(req: &Request) -> String {
    format!("hello: {}", req.uri().path())
}

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    let app = Route::new().at("/", hello);
    Server::new(TcpListener::bind("127.0.0.1:3000")).run(app).await
}
```
