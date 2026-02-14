---
tags: ["backend", "php", "microservices"]
---
# Framework: Hyperf

## Schema: Framework Specification

- framework: Hyperf
- category: backend
- language: PHP
- latest_supported_version: 3.x
- rendering_engine: N/A
- state_management: Hyperf DB
- router: Hyperf Router
- build_tool: Composer

---

## Core Stack

- **Coroutine**: Swoole based.

## Golden Snippet

```php
#[AutoController]
class IndexController
{
    public function index()
    {
        return 'Hello Hyperf.';
    }
}
```
