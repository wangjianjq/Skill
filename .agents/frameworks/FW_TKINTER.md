---
tags: ["desktop", "python", "gui"]
---
# Framework: tkinter

## Schema: Framework Specification

- framework: tkinter
- category: desktop
- language: Python
- latest_supported_version: 3.13+ (Python built-in)
- rendering_engine: Tk/Tcl
- state_management: Variable Classes (StringVar, IntVar, BooleanVar)
- router: N/A
- build_tool: uv | poetry (packaging with PyInstaller)

---

## 1. Project Initialization

### 1.1 Setup Command

tkinter is **built into Python** - no installation required!

```bash
# Modern approach with uv (for dependency management)
uv init my-tkinter-app
cd my-tkinter-app
# No need to add tkinter - it's bundled with Python

# Verify tkinter is available
python -m tkinter
```

**Options explanation:**

- tkinter is part of Python's standard library (no `pip install` needed)
- For packaging, add `pyinstaller` to dev dependencies
- Optional: `ttkthemes` for enhanced widget themes

### 1.2 Required Dependencies

```toml
# pyproject.toml (uv or poetry)
[project]
dependencies = []  # tkinter is built-in

[project.optional-dependencies]
dev = [
    "pyinstaller>=6.0",   # Packaging
    "ttkthemes>=3.2.2",   # Additional themes
]
```

---

## 2. Architecture

### 2.1 Directory Structure

```
my-tkinter-app/
├── src/
│   ├── main.py              # Application entry point
│   ├── views/               # UI components
│   │   ├── main_window.py   # Main window class
│   │   └── dialogs/         # Dialog windows
│   ├── controllers/         # Business logic (MVC pattern)
│   ├── models/              # Data models
│   ├── config.py            # Configuration
│   └── assets/              # Images, icons
├── tests/                   # Unit tests
└── pyproject.toml
```

### 2.2 Core Concepts

#### 2.2.1 Widget Hierarchy

tkinter follows a **parent-child widget hierarchy**:

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()  # Root window (parent)
frame = ttk.Frame(root)  # Frame (child of root)
button = ttk.Button(frame, text="Click")  # Button (child of frame)

frame.pack()
button.pack()
root.mainloop()
```

#### 2.2.2 Event-Driven Programming

tkinter uses **event bindings** for user interactions:

```python
def on_button_click():
    print("Button clicked!")

button = ttk.Button(root, text="Click Me", command=on_button_click)

# Alternative: bind events manually
def on_key_press(event):
    print(f"Key pressed: {event.char}")

root.bind("<Key>", on_key_press)
```

#### 2.2.3 Variable Classes (Reactive State)

Use `StringVar`, `IntVar`, `BooleanVar` for reactive updates:

```python
# Reactive variable
name_var = tk.StringVar(value="John")

# Entry bound to variable
entry = ttk.Entry(root, textvariable=name_var)

# Label updates automatically when name_var changes
label = ttk.Label(root, textvariable=name_var)

name_var.set("Jane")  # Both entry and label update!
```

---

## 3. Development Workflow

### 3.1 Development Mode

```bash
# Run application
uv run python src/main.py

# Using ttk (modern themed widgets)
# Prefer ttk over classic tk widgets for better look
```

### 3.2 Build for Production

```bash
# Using PyInstaller
uv run pyinstaller --onefile --windowed src/main.py

# macOS app bundle
uv run pyinstaller --onefile --windowed --icon=app.icns src/main.py

# Windows executable with custom icon
uv run pyinstaller --onefile --windowed --icon=app.ico src/main.py
```

### 3.3 Testing

```bash
# Unit tests (test logic, not GUI)
uv run pytest tests/

# Manual UI testing (tkinter has no built-in UI test framework)
```

---

## 4. Best Practices

### 4.1 Code Organization

1. **MVC Pattern**: Separate UI (View) from business logic (Controller)

   ```python
   # model.py
   class DataModel:
       def __init__(self):
           self.data = []
   
   # view.py
   class MainWindow(tk.Tk):
       def __init__(self, controller):
           super().__init__()
           self.controller = controller
   
   # controller.py
   class Controller:
       def __init__(self, model, view):
           self.model = model
           self.view = view
   ```

2. **Use ttk instead of tk widgets**:
   - `ttk.Button` instead of `tk.Button`
   - `ttk.Label` instead of `tk.Label`
   - Better cross-platform appearance

3. **Config-driven UI**: Store window settings in config files

### 4.2 Layout Management

Use **Grid** for complex layouts (recommended):

```python
# Grid layout (best for forms)
ttk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
ttk.Entry(root).grid(row=0, column=1)

ttk.Label(root, text="Email:").grid(row=1, column=0, sticky="w")
ttk.Entry(root).grid(row=1, column=1)
```

**Pack** for simple vertical/horizontal layouts:

```python
# Pack layout (simple stacking)
ttk.Label(root, text="Header").pack()
ttk.Button(root, text="Click").pack()
```

**Place** for absolute positioning (avoid in most cases):

```python
# Place layout (absolute positioning - not recommended)
button.place(x=50, y=100)
```

### 4.3 Performance

- **Avoid blocking operations**: Use `threading` for long tasks

  ```python
  import threading
  
  def long_task():
      # Heavy computation
      pass
  
  threading.Thread(target=long_task, daemon=True).start()
  ```

- **Update UI from main thread only**:

  ```python
  def update_ui():
      label.config(text="Updated")
  
  root.after(0, update_ui)  # Schedule UI update
  ```

### 4.4 Error Handling

Always handle exceptions in callbacks:

```python
def on_button_click():
    try:
        # Risky operation
        result = process_data()
        label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", str(e))
```

---

## 5. Common Patterns

### 5.1 Dialog Windows

```python
from tkinter import messagebox, simpledialog

# Show info dialog
messagebox.showinfo("Title", "Message")

# Ask yes/no
result = messagebox.askyesno("Confirm", "Are you sure?")

# Get user input
name = simpledialog.askstring("Input", "Enter your name:")
```

### 5.2 Menu Bar

```python
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Exit", command=root.quit)
```

### 5.3 Treeview (Table Display)

```python
tree = ttk.Treeview(root, columns=("Name", "Age"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

tree.insert("", "end", values=("Alice", 30))
tree.insert("", "end", values=("Bob", 25))

tree.pack()
```

---

## 6. Deployment

### 6.1 PyInstaller (Single Executable)

```bash
# Windows executable
pyinstaller --onefile --windowed --icon=app.ico src/main.py

# macOS app bundle
pyinstaller --onefile --windowed --icon=app.icns --osx-bundle-identifier=com.myapp src/main.py

# Linux binary
pyinstaller --onefile src/main.py
```

**Spec file** (advanced configuration):

```python
# main.spec
a = Analysis(['src/main.py'],
             pathex=[],
             binaries=[],
             datas=[('assets', 'assets')],  # Include assets
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=None,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)
exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas, [], name='MyApp', debug=False, bootloader_ignore_signals=False, strip=False, upx=True, upx_exclude=[], runtime_tmpdir=None, console=False, icon='app.ico')
```

### 6.2 Platform-Specific Notes

- **Windows**: Use `--windowed` to hide console window
- **macOS**: Requires code signing for distribution
- **Linux**: May need to bundle Tcl/Tk libraries on some distros

---

## 7. Critical Rules

1. **Framework Selection (tkinter vs PySide6/PyQt6)**:
   - **Use tkinter if**:
     - Simple GUI with basic widgets (forms, buttons, labels)
     - No external dependencies allowed (corporate environment)
     - Quick prototypes or utility scripts
     - Learning Python GUI basics
   - **Use PySide6/PyQt6 if**:
     - Complex UI with modern design (animations, custom widgets)
     - Need advanced features (QML, Graphics View, WebEngine)
     - Cross-platform consistency is critical
     - Long-term maintainability (better architecture support)

2. **Prefer ttk over tk**:
   - Always use `ttk.Button`, `ttk.Label` instead of `tk.Button`, `tk.Label`
   - Better native look and feel
   - Exception: `tk.Canvas`, `tk.Text` (no ttk equivalent)

3. **Memory Management**:
   - Widgets are managed by parent-child relationship
   - Destroying parent destroys all children
   - Use `destroy()` to clean up widgets

4. **Threading Rules**:
   - **Never** update GUI from non-main thread
   - Use `root.after()` to schedule updates from worker threads
   - Example:

     ```python
     def worker():
         result = expensive_computation()
         root.after(0, lambda: update_label(result))
     
     threading.Thread(target=worker, daemon=True).start()
     ```

5. **Event Loop**:
   - Call `root.mainloop()` only once in main thread
   - Use `root.quit()` to exit event loop
   - Avoid `root.destroy()` inside event handlers (can crash)

6. **Image Handling**:
   - **Critical**: Keep reference to PhotoImage objects

     ```python
     # ✅ Correct
     self.img = tk.PhotoImage(file="icon.png")
     label = ttk.Label(root, image=self.img)
     
     # ❌ Wrong (image will be garbage collected)
     label = ttk.Label(root, image=tk.PhotoImage(file="icon.png"))
     ```

7. **Configuration**:
   - Use `.config()` or `.configure()` to change widget properties
   - Example: `button.config(text="New Text", state="disabled")`

8. **Layout Managers**:
   - **Never mix** `pack()`, `grid()`, and `place()` in the same parent
   - Choose one layout manager per container

---

## 8. Comparison: tkinter vs PySide6/PyQt6

| Feature | tkinter | PySide6/PyQt6 |
|---------|---------|---------------|
| **Installation** | Built-in | Requires installation |
| **Learning Curve** | Low | Medium-High |
| **UI Complexity** | Simple to Medium | Medium to High |
| **Modern Look** | Basic (ttk themes) | Advanced (QML, stylesheets) |
| **Widgets** | ~30 basic widgets | 200+ widgets |
| **Licensing** | Python License (free) | LGPL / GPL/Commercial |
| **Performance** | Good for simple apps | Better for complex apps |
| **Documentation** | Standard Python docs | Qt official docs (extensive) |
| **Use Cases** | Utilities, prototypes | Production-grade apps |

**When to migrate from tkinter to Qt**:

- Your GUI has >10 windows
- Need custom graphics/animations
- Require database integration (Qt SQL)
- Want professional, polished UI

---

## 9. Golden Snippet

```python
# Modern tkinter app with MVC pattern
import tkinter as tk
from tkinter import ttk, messagebox

class Model:
    """Data model"""
    def __init__(self):
        self.counter = 0
    
    def increment(self):
        self.counter += 1
        return self.counter

class View(tk.Tk):
    """GUI View"""
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("tkinter Modern App")
        self.geometry("400x300")
        
        # Reactive variable
        self.counter_var = tk.StringVar(value="0")
        
        # Widgets
        ttk.Label(self, text="Counter:").pack(pady=10)
        ttk.Label(self, textvariable=self.counter_var, font=("Arial", 24)).pack()
        ttk.Button(self, text="Increment", command=self.on_increment).pack(pady=10)
        ttk.Button(self, text="Reset", command=self.on_reset).pack()
    
    def on_increment(self):
        self.controller.increment()
    
    def on_reset(self):
        self.controller.reset()
    
    def update_counter(self, value):
        self.counter_var.set(str(value))

class Controller:
    """Business logic"""
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def increment(self):
        count = self.model.increment()
        self.view.update_counter(count)
    
    def reset(self):
        self.model.counter = 0
        self.view.update_counter(0)

if __name__ == "__main__":
    model = Model()
    view = View(controller=None)
    controller = Controller(model, view)
    view.controller = controller
    view.mainloop()
```

---

## 10. Resources

- 📖 [Python tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- 🎨 [ttkthemes Gallery](https://ttkthemes.readthedocs.io/)
- 📦 [PyInstaller Documentation](https://pyinstaller.org/)
- 💡 [Real Python tkinter Tutorial](https://realpython.com/python-gui-tkinter/)
