---
name: rust-lint
description: Rust code quality check - Use Clippy and Rustfmt to ensure Rust code standards and performance optimization
---

# Rust Lint Skill

## 📋 Overview

Use Rust official toolchain to check code quality:

- **Clippy**: Smart code checks (450+ rules)
- **Rustfmt**: Code formatting

## 🔧 Prerequisites

| Tool | Min Version | Installation |
|------|-------------|--------------|
| Rust | 1.70+ | `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` |
| Clippy | - | `rustup component add clippy` |
| Rustfmt | - | `rustup component add rustfmt` |

## 🚀 Usage

**Run Clippy:**

```bash
.\.agent\skills\rust-lint\scripts\lint.ps1
```

**Auto-fix:**

```bash
.\.agent\skills\rust-lint\scripts\lint.ps1 -Fix
```

**Format code:**

```bash
.\.agent\skills\rust-lint\scripts\format.ps1
```

## 🎯 What It Checks

### Performance Optimization

- ✅ Avoid unnecessary clones
- ✅ Use iterators instead of loops
- ✅ String handling optimization
- ✅ Collection operation efficiency

### Security

- ✅ Unused unsafe code
- ✅ Integer overflow detection
- ✅ Null pointer dereference
- ✅ Lifetime issues

### Idiomatic Rust

- ✅ Pattern matching recommendations
- ✅ Option/Result usage
- ✅ Error handling best practices
- ✅ Trait implementation suggestions

## 📊 Output Example

```
🦀 Rust Lint - Checking project...

warning: unnecessary use of `clone`
  --> src/main.rs:15:18
   |
15 |     let data = items.clone();
   |                      ^^^^^^^^ help: remove this
   |
   = note: `#[warn(clippy::unnecessary_clone)]` on by default

error: indexing may panic
  --> src/lib.rs:42:13
   |
42 |     let x = arr[5];
   |             ^^^^^^
   |
   = help: consider using `.get()` or `.get_mut()`

📊 Results:
   ❌ Errors: 1
   ⚠️  Warnings: 3
```

## ⚙️ Configuration

Create `clippy.toml`:

```toml
cognitive-complexity-threshold = 30
too-many-arguments-threshold = 8

disallowed-methods = [
    "std::env::set_var",  # Unsafe environment variable setting
]

# Allowed lints
allow = [
    "clippy::module_name_repetitions",
]

# Warning level lints
warn = [
    "clippy::pedantic",
    "clippy::nursery",
]

# Denied lints
deny = [
    "clippy::unwrap_used",
    "clippy::expect_used",
]
```

Create `rustfmt.toml`:

```toml
max_width = 100
indent_style = "Block"
use_small_heuristics = "Default"
imports_granularity = "Crate"
```

## 🔗 Related Resources

- [Clippy Lints List](https://rust-lang.github.io/rust-clippy/master/)
- [Rustfmt Configuration](https://rust-lang.github.io/rustfmt/)
