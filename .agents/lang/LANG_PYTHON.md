# Language: Python

## Schema: Language Specification

- language: Python
- category: programming_language
- latest_supported_version: 3.12+
- package_manager_modern: uv | poetry
- package_manager_legacy: pip | pipenv
- linter_modern: ruff
- linter_legacy: flake8 + black + isort
- type_system: gradual (optional static typing)
- config_file_modern: pyproject.toml
- config_file_legacy: requirements.txt

---

## [Modern] (v3.12+, uv-based)

- **Env**: `uv` or `poetry`. `pyproject.toml` is mandatory.
- **Lint**: `ruff` (Fast, all-in-one).
- **Standard**: Use `typing.Annotated`, `typing.TypeAlias` (v3.12+ features).

## [Legacy] (v3.8 - v3.11, pip-based)

- **Env**: `pip` + `venv` or `pipenv`. `requirements.txt` is common.
- **Lint**: `flake8`, `black`, `isort`.
- **Standard**: Use `typing.Dict`, `typing.List` (instead of `dict[]`, `list[]`).
- **Compatibility**: Ensure `__future__.annotations` is imported if using backported types.
