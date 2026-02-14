---
tags: ["backend", "php", "enterprise"]
---
# Framework: Symfony

## Schema: Framework Specification

- framework: Symfony
- category: backend
- language: PHP
- latest_supported_version: 7.x
- rendering_engine: Twig
- state_management: Doctrine ORM
- router: Symfony Router
- build_tool: Composer

---

## Core Stack

- **Components**: Highly reusable.

## Golden Snippet

```php
#[Route('/lucky/number')]
public function number(): Response
{
    $number = random_int(0, 100);
    return new Response('Lucky number: '.$number);
}
```
