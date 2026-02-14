---
tags: ["backend", "php", "fullstack"]
---
# Framework: Laravel

## Schema: Framework Specification

- framework: Laravel
- category: backend
- language: PHP
- latest_supported_version: 11+
- rendering_engine: Blade
- state_management: Eloquent ORM
- router: Laravel Router
- build_tool: Composer

---

## [Modern] (v11+, PHP 8.2+)

- **Version**: v11+.
- **Config**: Minimal config files (most setup in `bootstrap/app.php`).
- **Routing**: API routing streamlined.

### Modern Snippet

```php
Route::get('/api/data', fn () => ['status' => 'Modern Laravel']);
```

## [Legacy] (v8 - v10)

- **Config**: Full `config/` directory.
- **Auth**: `Laravel Breeze` or `Jetstream` (Standard).
