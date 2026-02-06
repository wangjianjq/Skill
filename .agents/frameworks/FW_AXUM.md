---
tags: ["backend", "rust", "tokio"]
---
# Framework: Axum

## Schema: Framework Specification

- framework: Axum
- category: backend
- language: Rust
- latest_supported_version: 0.7+
- rendering_engine: N/A
- state_management: N/A
- router: Axum Router (Tower-based)
- build_tool: Cargo

---

## Core Stack

- **Ecosystem**: Tokio based.

## Golden Snippet

```rust
use axum::{routing::get, Router};

#[tokio::main]
async fn main() {
    let app = Router::new().route("/", get(|| async { "Hello" }));
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
```
