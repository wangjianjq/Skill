---
tags: ["python", "standard-library", "pathlib", "threading"]
---
# Knowledge: Python Standard Library (Critical Modules)

## 1. File & Paths (`pathlib`)

Prefer `Path` objects over `os.path` strings.

* `Path.cwd()`: Current directory.
* `path.exists()`, `path.is_file()`, `path.mkdir(parents=True, exist_ok=True)`.
* `path.glob("*.mp3")`: Pattern matching.

## 2. JSON & Data (`json`)

* `json.dump(data, f, indent=4, ensure_ascii=False)`: Human-readable saving.
* `json.loads(string)`: Parsing.

## 3. Concurrency (`threading`)

Critical for keeping GUI responsive.

* `threading.Thread(target=func, args=(x,), daemon=True).start()`.
* **Warning**: Never update Tkinter widgets directly from a background thread. Use `root.after(0, update_func)` or a `queue.Queue`.

## 4. Internationalization (`gettext`)

* Standard for multi-language apps.
* Use `_("Key")` as the translation function.

## 5. Subprocess (`subprocess`)

* `subprocess.run(["command", "arg"], capture_output=True, text=True)`.
* Used for tools like `fpcalc`.
