# Database: SQLite

## [Modern] (v3.45+, JSONB)

* **Features**: `JSONB` native storage (v3.45+ binary format).
* **Patterns**: High-performance local storage, Cloudflare D1 compatibility.

### Modern Golden Snippet

```sql
-- Using SQLite 3.45+ JSONB
SELECT json_extract(metadata, '$.author') FROM notes;
```

## [Legacy] (Standard SQLite)

* **Features**: Text-based JSON storage.
* **Compatibility**: Universal support.
