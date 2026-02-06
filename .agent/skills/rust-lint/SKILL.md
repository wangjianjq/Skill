---
name: rust-lint
description: Rust 代码质量检查 - 使用 Clippy 和 Rustfmt 确保 Rust 代码规范和性能优化
---

# Rust Lint Skill

## 📋 概述

使用 Rust 官方工具链检查代码质量：

- **Clippy**: 智能代码检查（450+ 规则）
- **Rustfmt**: 代码格式化

## 🔧 前置条件

| 工具 | 最低版本 | 安装命令 |
|-----|---------|---------|
| Rust | 1.70+ | `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` |
| Clippy | - | `rustup component add clippy` |
| Rustfmt | - | `rustup component add rustfmt` |

## 🚀 使用方法

**运行 Clippy:**

```bash
.\.agent\skills\rust-lint\scripts\lint.ps1
```

**自动修复:**

```bash
.\.agent\skills\rust-lint\scripts\lint.ps1 -Fix
```

**格式化代码:**

```bash
.\.agent\skills\rust-lint\scripts\format.ps1
```

## 🎯 检查内容

### 性能优化

- ✅ 避免不必要的克隆
- ✅ 使用迭代器而非循环
- ✅ 字符串处理优化
- ✅ 集合操作效率

### 安全性

- ✅ 未使用的 unsafe 代码
- ✅ 整数溢出检测
- ✅ 空指针解引用
- ✅ 生命周期问题

### Idiomatic Rust

- ✅ 模式匹配推荐
- ✅ Option/Result 使用
- ✅ 错误处理最佳实践
- ✅ Trait 实现建议

## 📊 输出示例

```
🦀 Rust Lint - 检查项目...

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

📊 结果:
   ❌ 错误: 1 个
   ⚠️  警告: 3 个
```

## ⚙️ 配置文件

创建 `clippy.toml`:

```toml
cognitive-complexity-threshold = 30
too-many-arguments-threshold = 8

disallowed-methods = [
    "std::env::set_var",  # 不安全的环境变量设置
]

# 允许的 lints
allow = [
    "clippy::module_name_repetitions",
]

# 警告级别的 lints
warn = [
    "clippy::pedantic",
    "clippy::nursery",
]

# 禁止级别的 lints
deny = [
    "clippy::unwrap_used",
    "clippy::expect_used",
]
```

创建 `rustfmt.toml`:

```toml
max_width = 100
indent_style = "Block"
use_small_heuristics = "Default"
imports_granularity = "Crate"
```

## 🔗 相关资源

- [Clippy Lints 列表](https://rust-lang.github.io/rust-clippy/master/)
- [Rustfmt 配置](https://rust-lang.github.io/rustfmt/)
