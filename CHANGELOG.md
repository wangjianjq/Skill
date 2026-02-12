# CHANGELOG

## 2026-02-11

- chore: 项目初始化完成并准备分发 / Project initialization completed for distribution.

## 2026-02-12

- fix: 修复核心目录匹配错误（`.agent/skills/` → `.agents/skills/`），避免将技能目录误判为非核心文件 / Fix core path matching (`.agent/skills/` → `.agents/skills/`) to avoid misclassifying the skills directory as non-core.
- refactor: 减少项目扫描中的重复分类计算并移除未使用导入，提升脚本可读性与微小性能 / Reduce duplicate classification checks in project scan and remove an unused import for cleaner code and minor performance improvement.
- fix: 修复通配目录模式 `*.egg-info/` 的匹配逻辑，确保扫描器可识别以 `.egg-info` 结尾的构建目录 / Fix wildcard directory matching for `*.egg-info/` so scanner correctly recognizes build directories ending with `.egg-info`.
