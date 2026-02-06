---
tags: ["desktop", "python", "qt6"]
---
# Framework: PySide6

## Schema: Framework Specification

- framework: PySide6
- category: desktop
- language: Python
- latest_supported_version: 6.7+
- rendering_engine: Qt 6 (C++ renderer)
- state_management: Qt Signals/Slots
- router: N/A
- build_tool: uv | poetry

---

## 1. Project Initialization

### 1.1 Setup Command

```bash
# Modern approach with uv
uv init my-pyside6-app
cd my-pyside6-app
uv add pyside6

# Alternative: Using poetry
poetry new my-pyside6-app
cd my-pyside6-app
poetry add pyside6
```

**Options explanation:**

- `pyside6`: Core Qt 6 bindings for Python (official Qt Company package)
- Optional: `pyside6-addons` for additional Qt modules
- Optional: `qt-material` for Material Design themes

### 1.2 Required Dependencies

```toml
# pyproject.toml (uv or poetry)
[project]
dependencies = [
    "pyside6>=6.7.0",
]

[project.optional-dependencies]
dev = [
    "pytest-qt>=4.4.0",    # Testing framework
    "pyinstaller>=6.0",    # Packaging
    "black>=24.0",         # Code formatting
]
```

---

## 2. Architecture

### 2.1 Directory Structure

```
my-pyside6-app/
├── src/
│   ├── main.py              # Application entry point
│   ├── ui/                  # UI components
│   │   ├── main_window.py   # Main window class
│   │   ├── dialogs/         # Dialog windows
│   │   └── widgets/         # Custom widgets
│   ├── models/              # Data models
│   ├── controllers/         # Business logic (MVC pattern)
│   ├── resources/           # Qt resources (.qrc compiled)
│   │   ├── icons/
│   │   ├── images/
│   │   └── styles.qss       # Qt Stylesheets
│   └── utils/               # Utilities
├── tests/                   # pytest-qt tests
├── resources.qrc            # Qt Resource file
└── pyproject.toml
```

### 2.2 Core Concepts

#### 2.2.1 Widgets vs QML

**Qt Widgets** (Traditional approach):

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click Me", self)
```

**QML** (Declarative UI, recommended for modern apps):

```python
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.load("main.qml")
```

#### 2.2.2 Signals and Slots

Core communication mechanism in Qt:

```python
from PySide6.QtCore import QObject, Signal, Slot

class Worker(QObject):
    # Define signal
    progress = Signal(int)
    
    def do_work(self):
        for i in range(100):
            self.progress.emit(i)  # Emit signal

# Connect signal to slot
worker = Worker()
worker.progress.connect(lambda value: print(f"Progress: {value}%"))
```

#### 2.2.3 Parent-Child Ownership

Qt manages memory through parent-child relationships:

```python
# Parent owns child - child deleted when parent deleted
window = QMainWindow()  # Parent
button = QPushButton("Click", window)  # Child (parent specified)

# Manual deletion required if no parent
orphan = QPushButton("Orphan")
orphan.deleteLater()  # Clean up manually
```

---

## 3. Development Workflow

### 3.1 Development Mode

```bash
# Run with hot-reload (using Qt Designer for UI)
uv run python src/main.py

# Using Qt Designer for visual UI editing
designer  # Launch Qt Designer (if installed)

# Compile .ui files to .py
pyside6-uic form.ui -o ui_form.py
```

### 3.2 Build for Production

```bash
# Using PyInstaller
uv run pyinstaller --onefile --windowed src/main.py

# Using Briefcase (cross-platform)
briefcase create
briefcase build
briefcase package
```

Configuration for PyInstaller:

```python
# spec file: main.spec
a = Analysis(['src/main.py'],
             pathex=[],
             binaries=[],
             datas=[('src/resources', 'resources')],
             hiddenimports=['PySide6.QtCore', 'PySide6.QtGui', 'PySide6.QtWidgets'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=None,
             noarchive=False)
```

### 3.3 Testing

```bash
# Unit tests with pytest-qt
uv run pytest tests/

# Coverage report
uv run pytest --cov=src tests/
```

**Example test:**

```python
import pytest
from PySide6.QtWidgets import QPushButton

def test_button_click(qtbot):
    button = QPushButton("Click Me")
    qtbot.addWidget(button)
    
    clicked = False
    def on_click():
        nonlocal clicked
        clicked = True
    
    button.clicked.connect(on_click)
    qtbot.mouseClick(button, Qt.LeftButton)
    assert clicked
```

---

## 4. Best Practices

### 4.1 Code Organization

1. **MVC/MVVM Pattern**: Separate UI (View) from business logic (Controller/ViewModel)

   ```python
   # model.py
   class DataModel(QObject):
       data_changed = Signal(str)
   
   # view.py
   class MainWindow(QMainWindow):
       pass
   
   # controller.py
   class Controller:
       def __init__(self, model, view):
           self.model = model
           self.view = view
   ```

2. **Single Responsibility**: One class per file for complex widgets
3. **Resource Management**: Use .qrc for all assets (icons, images, styles)

### 4.2 Performance

#### 4.2.1 Event Loop Optimization

- **Long operations**: Move to QThread to avoid UI freezing

  ```python
  from PySide6.QtCore import QThread
  
  class Worker(QThread):
      def run(self):
          # Heavy computation here
          pass
  
  worker = Worker()
  worker.start()  # Runs in background thread
  ```

- **Avoid**: `QApplication.processEvents()` (blocks event loop)

#### 4.2.2 Memory Management

- **Use `deleteLater()`** instead of `del` for Qt objects
- **Disconnect signals** when objects are destroyed
- **Weak references** for circular dependencies

### 4.3 Security

1. **Input Validation**: Always validate user input before processing

   ```python
   text = line_edit.text()
   if not text.isalnum():
       QMessageBox.warning(self, "Invalid Input", "Only alphanumeric characters allowed")
       return
   ```

2. **SQL Injection Prevention**: Use QSqlQuery with placeholders
3. **File Path Sanitization**: Use `Path.resolve()` to prevent directory traversal

### 4.4 Testing

- **Unit Tests**: Use `pytest-qt` for widget testing
- **Integration Tests**: Test signal-slot connections
- **UI Tests**: Use `QTest` for simulating user interactions

  ```python
  from PySide6.QtTest import QTest
  
  QTest.keyClicks(widget, "Hello")  # Simulate typing
  QTest.mouseClick(button, Qt.LeftButton)  # Simulate click
  ```

---

## 5. Common Patterns

### 5.1 Model-View-Delegate Pattern

**Use Case**: Displaying data in tables/lists with custom rendering

```python
from PySide6.QtCore import QAbstractTableModel
from PySide6.QtWidgets import QTableView

class CustomTableModel(QAbstractTableModel):
    def rowCount(self, parent=None):
        return len(self.data)
    
    def columnCount(self, parent=None):
        return len(self.data[0])
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.data[index.row()][index.column()]

view = QTableView()
model = CustomTableModel()
view.setModel(model)
```

### 5.2 Singleton Application

**Use Case**: Ensure only one instance of app is running

```python
from PySide6.QtCore import QLockFile, QDir

class SingletonApp:
    def __init__(self):
        self.lock_file = QLockFile(QDir.temp().filePath("myapp.lock"))
        
    def is_running(self):
        return not self.lock_file.tryLock()
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

**Pro Tips:**

- Use `--add-data` for resource files
- Use `--hidden-import` for dynamic imports
- Test on target OS (Windows DLLs differ from Linux .so)

### 6.2 Briefcase (Cross-Platform Packaging)

```toml
# pyproject.toml
[tool.briefcase]
project_name = "My PySide6 App"
bundle = "com.example"

[tool.briefcase.app.myapp]
formal_name = "My App"
description = "A PySide6 desktop application"
sources = ['src']
requires = ['pyside6>=6.7.0']
```

```bash
# Create platform-specific installer
briefcase create      # Generate platform template
briefcase build       # Build app
briefcase package     # Create installer (.msi, .dmg, .deb)
```

---

## 7. Critical Rules

1. **Framework Selection (PySide6 vs PyQt6)**:
   - **Use PySide6 if**: LGPL license is acceptable, want official Qt Company support, prefer LGPL over GPL
   - **Use PyQt6 if**: Need mature ecosystem, GPL/Commercial license acceptable, have existing PyQt codebase
   - **API Compatibility**: ~95% compatible between PySide6 and PyQt6, migration is relatively easy
   - **Import difference**: `from PySide6.QtWidgets import *` vs `from PyQt6.QtWidgets import *`

2. **Choice Criteria for PySide6**:
   - ✅ **LGPL License**: Free for commercial use (LGPL v3)
   - ✅ **Official Support**: Maintained by Qt Company
   - ✅ **Modern Qt**: Always up-to-date with latest Qt releases
   - ⚠️ **Ecosystem**: Smaller community compared to PyQt

3. **Never Mix Frameworks**: Do not use PySide6 and PyQt6 in the same project (binary incompatibility)

4. **Memory Management**:
   - Parent-child ownership is automatic (child deleted with parent)
   - Avoid circular references between QObjects
   - Use `deleteLater()` for safe deletion

5. **Threading**:
   - **Always use `QThread`**, not Python's `threading` module
   - UI updates MUST happen in main thread
   - Use signals to communicate from worker thread to UI

6. **Resource System**:
   - Use Qt Resource System (.qrc) for all assets
   - Compile with `pyside6-rcc resources.qrc -o resources_rc.py`
   - Import compiled resources: `import resources_rc`

7. **Event Loop**:
   - Call `QApplication.exec()` only once in main thread
   - Avoid blocking operations in event handlers
   - Use `QTimer` for periodic tasks, not `while True` loops
