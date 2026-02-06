---
tags: ["backend", "python", "fullstack"]
---
# Framework: Django

## Schema: Framework Specification

- framework: Django
- category: backend
- language: Python
- latest_supported_version: 5.1+
- rendering_engine: Django Templates
- state_management: ORM/Session
- router: URLconf
- build_tool: uv | poetry

---

## [Modern] (v5.0+, Python 3.10+)

- **Async**: Native support for async views and ORM queries (`aget()`, `acreate()`).
- **Forms**: `Form.template_name` for easy UI customization.

### Modern Async Snippet

```python
async def my_view(request):
    data = await MyModel.objects.aget(id=1)
    return JsonResponse(data.to_dict())
```

## [Legacy] (v3.2 - v4.2)

- **Pattern**: Synchronous logic only.
- **Deployment**: WSGI-based.
