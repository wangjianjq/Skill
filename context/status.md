# 项目状态快照

> **⚠️ 注意**: 本文件由 `context/auto_status.py` 自动生成和维护  
> 请勿手动编辑 "自动生成区域"，可以编辑 "手动维护区域"

---

## 📊 自动生成区域

**生成时间**: 2026-02-09 02:33  
**项目规模**: 392 个文件，36,258 行代码

### 技术栈
_未检测到标准依赖文件_

### 项目结构（最多 2 层深度）
```
- ./
  - AGENTS.md
  - CHANGELOG.md
  - CLAUDE.md
  - CONVENTIONS.md
  - GEMINI.md
  - .agent/
  - .agents/
    - AGENTS_ROOT.md
    - BMAD_BOOTSTRAP.md
  - .claude/
    - CLAUDE.md
    - settings.json
  - .codex/
    - instructions.md
  - .github/
    - copilot-instructions.md
  - .idea/
    - ai-instructions.md
  - .zed/
    - ai.md
  - bmad/
  - docs/
```

---

## ✍️ 手动维护区域

### 当前开发焦点

_请在此处记录当前正在进行的工作，例如：_

- 正在重构用户认证模块
- 修复登录页面的响应式布局问题

### 已知问题

_可选：记录当前已知但未修复的问题_

### 下一步计划

_可选：记录即将进行的开发任务_

---

## 🔄 更新此文件

运行以下命令刷新自动生成的内容：

```bash
# Windows PowerShell
python context\auto_status.py

# Linux/Mac
python3 context/auto_status.py
```

**推荐**：设置为 Git hooks 自动触发
```bash
# .git/hooks/post-commit
python context/auto_status.py
```
