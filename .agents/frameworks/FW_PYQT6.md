---
tags: ["desktop", "python", "qt6"]
---
# Framework: PyQt6

## Schema: Framework Specification

- framework: PyQt6
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
uv init my-pyqt6-app
cd my-pyqt6-app
uv add pyqt6

# Alternative: Using poetry
poetry new my-pyqt6-app
cd my-pyqt6-app
poetry add pyqt6
```

**Options explanation:**

- `pyqt6`: Core Qt 6 bindings for Python (Riverbank Computing)
- Optional: `pyqt6-tools` for Qt Designer, pyuic, etc.
- Optional: `pyqt6-qt6` for bundled Qt libraries

### 1.2 Required Dependencies

```toml
# pyproject.toml (uv or poetry)
[project]
dependencies = [
    "pyqt6>=6.7.0",
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
my-pyqt6-app/
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
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click Me", self)
```

**QML** (Declarative UI, recommended for modern apps):

```python
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtGui import QGuiApplication

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.load("main.qml")
```

#### 2.2.2 Signals and Slots (PyQt6 Specific Syntax)

Core communication mechanism in Qt:

```python
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot

class Worker(QObject):
    # Define signal (note: pyqtSignal, not Signal)
    progress = pyqtSignal(int)
    
    def do_work(self):
        for i in range(100):
            self.progress.emit(i)  # Emit signal

# Connect signal to slot
worker = Worker()
worker.progress.connect(lambda value: print(f"Progress: {value}%"))
```

**Key Difference from PySide6**: Use `pyqtSignal` and `pyqtSlot` instead of `Signal` and `Slot`

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
# Run application
uv run python src/main.py

# Using Qt Designer for visual UI editing
designer  # Or: pyqt6-tools designer

# Compile .ui files to .py (PyQt6 specific tool)
pyuic6 form.ui -o ui_form.py
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
             hiddenimports=['PyQt6.QtCore', 'PyQt6.QtGui', 'PyQt6.QtWidgets'],
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
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt

def test_button_click(qtbot):
    button = QPushButton("Click Me")
    qtbot.addWidget(button)
    
    clicked = False
    def on_click():
        nonlocal clicked
        clicked = True
    
    button.clicked.connect(on_click)
    qtbot.mouseClick(button, Qt.MouseButton.LeftButton)
    assert clicked
```

---

## 4. Best Practices

### 4.1 Code Organization

1. **MVC/MVVM Pattern**: Separate UI (View) from business logic (Controller/ViewModel)

   ```python
   # model.py
   from PyQt6.QtCore import QObject, pyqtSignal
   
   class DataModel(QObject):
       data_changed = pyqtSignal(str)
   
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
  from PyQt6.QtCore import QThread
  
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
  from PyQt6.QtTest import QTest
  from PyQt6.QtCore import Qt
  
  QTest.keyClicks(widget, "Hello")  # Simulate typing
  QTest.mouseClick(button, Qt.MouseButton.LeftButton)  # Simulate click
  ```

---

## 5. Common Patterns

### 5.1 Model-View-Delegate Pattern

**Use Case**: Displaying data in tables/lists with custom rendering

```python
from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtWidgets import QTableView

class CustomTableModel(QAbstractTableModel):
    def rowCount(self, parent=None):
        return len(self.data)
    
    def columnCount(self, parent=None):
        return len(self.data[0])
    
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.data[index.row()][index.column()]

view = QTableView()
model = CustomTableModel()
view.setModel(model)
```

### 5.2 Singleton Application

**Use Case**: Ensure only one instance of app is running

```python
from PyQt6.QtCore import QLockFile, QDir

class SingletonApp:
    def __init__(self):
        self.lock_file = QLockFile(QDir.tempPath() + "/myapp.lock")
        
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
project_name = "My PyQt6 App"
bundle = "com.example"

[tool.briefcase.app.myapp]
formal_name = "My App"
description = "A PyQt6 desktop application"
sources = ['src']
requires = ['pyqt6>=6.7.0']
```

```bash
# Create platform-specific installer
briefcase create      # Generate platform template
briefcase build       # Build app
briefcase package     # Create installer (.msi, .dmg, .deb)
```

---

## 7. Critical Rules

1. **Framework Selection (PyQt6 vs PySide6)**:
   - **Use PyQt6 if**: Need mature ecosystem with extensive community resources, GPL/Commercial dual license acceptable, migrating from PyQt5
   - **Use PySide6 if**: LGPL license preferred, want official Qt Company support, starting new project
   - **API Compatibility**: ~95% compatible between PyQt6 and PySide6, main difference is signal/slot syntax
   - **Import difference**: `from PyQt6.QtWidgets import *` vs `from PySide6.QtWidgets import *`

2. **Choice Criteria for PyQt6**:
   - ✅ **Mature Ecosystem**: Larger community, more tutorials, established best practices
   - ✅ **Backward Compatibility**: Easier migration from PyQt5
   - ✅ **Commercial Support**: Dual license (GPL v3 for open source, commercial license available)
   - ⚠️ **License**: GPL v3 requires open-sourcing derivative works (unless commercial license purchased)

3. **Signal/Slot Syntax Differences**:
   - PyQt6: `pyqtSignal`, `pyqtSlot`
   - PySide6: `Signal`, `Slot`
   - Example:

     ```python
     # PyQt6
     from PyQt6.QtCore import pyqtSignal
     class MyClass(QObject):
         my_signal = pyqtSignal(int)
     
     # PySide6 equivalent
     from PySide6.QtCore import Signal
     class MyClass(QObject):
         my_signal = Signal(int)
     ```

4. **Never Mix Frameworks**: Do not use PyQt6 and PySide6 in the same project (binary incompatibility)

5. **Memory Management**:
   - Parent-child ownership is automatic (child deleted with parent)
   - Avoid circular references between QObjects
   - Use `deleteLater()` for safe deletion

6. **Threading**:
   - **Always use `QThread`**, not Python's `threading` module
   - UI updates MUST happen in main thread
   - Use signals to communicate from worker thread to UI

7. **Resource System**:
   - Use Qt Resource System (.qrc) for all assets
   - Compile with `pyrcc6 resources.qrc -o resources_rc.py` (PyQt6 tool)
   - Import compiled resources: `import resources_rc`

8. **Event Loop**:
   - Call `QApplication.exec()` only once in main thread (note: `exec()` not `exec_()` in Qt6)
   - Avoid blocking operations in event handlers
   - Use `QTimer` for periodic tasks, not `while True` loops

9. **Qt 6 Enum Changes**:
   - Use fully qualified enum names: `Qt.MouseButton.LeftButton` instead of `Qt.LeftButton`
   - Use `Qt.ItemDataRole.DisplayRole` instead of `Qt.DisplayRole`
   - This is a breaking change from PyQt5
