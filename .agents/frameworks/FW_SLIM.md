---
tags: ["backend", "php", "micro"]
---
# Framework: Slim

## Schema: Framework Specification

- framework: Slim
- category: backend
- language: PHP
- latest_supported_version: 4.x
- rendering_engine: N/A
- state_management: N/A
- router: Slim Router (PSR-7)
- build_tool: Composer

---

## Core Stack

- **PSR**: PSR-7 compatible.

## Golden Snippet

```php
$app->get('/hello/{name}', function (Request $request, Response $response, array $args) {
    $name = $args['name'];
    $response->getBody()->write("Hello, $name");
    return $response;
});
```
