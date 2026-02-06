---
tags: ["gui", "tkinter", "python-std"]
---
# Knowledge: Tkinter & TTK Reference

## Core Hierarchy

* `tk.Tk()`: Root window.
* `ttk.Frame`: Container for grouping widgets.
* `ttk.Label`, `ttk.Button`, `ttk.Entry`, `ttk.Combobox`, `ttk.Treeview`.

## Geometry Managers

1. **Grid (Recommended)**: `grid(row=n, column=m, sticky='nsew', padx=5, pady=5)`.
    * Use `columnconfigure(index, weight=1)` on parent for resizing.
2. **Pack**: `pack(side=TOP, fill=X, expand=True)`.
3. **Place**: Avoid unless absolute positioning is required.

## Event Handling

* `widget.bind("<Button-1>", callback)`: Mouse click.
* `widget.bind("<Return>", callback)`: Enter key.
* `widget.bind("<<ComboboxSelected>>", callback)`: Specific to Combobox.

## Themed Widgets (TTK)

Always prefer `tkinter.ttk` widgets for a native look.
Example Treeview (Table):

```python
tree = ttk.Treeview(root, columns=('Name', 'Size'), show='headings')
tree.heading('Name', text='Filename')
tree.insert('', 'end', values=('song.mp3', '5MB'))
```

## Common Options

* `sticky`: 'n', 's', 'e', 'w' (North, South, East, West).
* `compound`: 'left', 'right' (for image+text).
* `state`: 'normal', 'disabled', 'readonly'.

## Concurrency Model

> **CRITICAL**: Do NOT use `asyncio` with Tkinter. It complicates the event loop.

1. **Threading**: Use `threading.Thread` for long-running blocking operations (network, disk I/O).
2. **UI Updates**: NEVER touch UI widgets from a background thread.
3. **Bridge**: Use `root.after(0, callback)` or a `queue.Queue` to marshal data back to the main thread for UI updates.
