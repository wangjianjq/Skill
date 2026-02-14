---
tags: ["backend", "rust", "productive"]
---
# Framework: Rocket

## Schema: Framework Specification

- framework: Rocket
- category: backend
- language: Rust
- latest_supported_version: 0.5+
- rendering_engine: N/A
- state_management: N/A
- router: Rocket Router
- build_tool: Cargo

---

## Core Stack

- **Macros**: Heavily macro based.

## Golden Snippet

```rust
#[macro_use] extern crate rocket;

#[get("/")]
fn index() -> &'static str { "Hello, world!" }

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index])
}
```
