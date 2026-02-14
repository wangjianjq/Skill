---
tags: ["backend", "rust", "performance"]
---
# Framework: Actix Web

## Schema: Framework Specification

- framework: Actix Web
- category: backend
- language: Rust
- latest_supported_version: 4.x
- rendering_engine: N/A
- state_management: Actor Model
- router: Actix Router
- build_tool: Cargo

---

## Core Stack

- **Actor**: Actor model based.

## Golden Snippet

```rust
use actix_web::{get, App, HttpServer, Responder};

#[get("/")]
async fn index() -> impl Responder {
    "Hello world!"
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(index))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}
```
