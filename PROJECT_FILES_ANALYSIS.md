# 项目文件分类分析报告

基于对项目目录的完整扫描（2026-02-09）

## 文件分类定义

### 核心引导/索引文件

- AGENTS.md, GEMINI.md, CLAUDE.md 等主引导文件
- README 系列文档
- .agents/, .claude/, bmad/ 等配置目录
- context/ 系统文件
- .agent/skills/ 目录
- 工具脚本（setup.bat, ResetAG.bat 等）

### 临时/垃圾文件

- Python 缓存：*.pyc,*.pyo, __pycache__/
- 编辑器临时文件：*.swp,*.tmp, *~, .DS_Store
- 日志文件：*.log
- 构建产物：dist/, build/, *.egg-info/
- 依赖管理：node_modules/, package-lock.json

### 非核心文件

- 与引导系统无关的辅助文件
- 测试文件、示例代码等

---

## 扫描结果摘要

__总文件数__: 392 个文件
__核心文件__: ~200 个文件（估算）
__临时文件__: 0 个（项目很干净）
__非核心文件__: ~190 个文件

---

## 非核心文件详情（按目录分类）

### bmad/ 目录

这是 BMAD 框架的核心，虽然被标记为"核心"，但以下子目录可能包含示例和模板：

__可能的非必需文件__：

- bmad/assets/ - 资源文件
- bmad/examples/ - 示例代码
- bmad/templates/ - 模板文件

__建议__: 保留框架核心，仅在确认无用时删除示例

---

### .agent/workflows/ 目录

包含大量工作流文件（~60+ 文件）

__示例工作流__：

- create-prd.md, create-epics-and-stories.md
- dev-story.md, qa-automate.md
- research.md, brainstorming.md

__评估__:

- 如果您不使用某些 workflow，可以删除对应的 .md 文件
- 核心 workflow 建议保留：/aaaa, /rrrr, /analyst, /dev

__潜在节省__: ~50+ 个未使用的 workflow 文件

---

### .agent/skills/ 目录

包含 17 个 skill，每个 skill 通常有：

- SKILL.md（必需）
- scripts/ 目录（.ps1 和 .sh 脚本）
- examples/（可选）

__可以删除的 skills__（如果不使用）：

- ai-agent-lint - 如果不开发 AI Agent
- docker-lint - 如果不使用 Docker
- k8s-lint - 如果不使用 Kubernetes
- rust-lint - 如果不用 Rust
- sql-lint - 如果不用 SQL
- db-migrate, owasp-scan, vuln-scan - 根据需求

__潜在节省__: 删除 10 个不用的 skills，约 30-50 个文件

---

### docs/ 目录

可能包含文档和教程

__建议__: 查看是否有重复或过时的文档

---

### 根目录临时脚本

今天创建的分析脚本：

- find_today_changes.py
- scan_project_files.py

__建议__: 分析完成后可删除

---

## 建议清理清单

### ✅ 可以安全删除

1. __临时分析脚本__（2 个文件）：
   - find_today_changes.py
   - scan_project_files.py

2. __未使用的 workflows__（按需）：
   - 检查 `.agent/workflows/` 下不用的工作流

3. __未使用的 skills__（按需）：
   - 根据技术栈删除不需要的 skills

### ⚠️ 谨慎删除

1. __bmad/examples/__ - 示例代码可作为参考
2. __bmad/templates/__ - 模板文件可能被框架使用

### ❌ 不要删除

1. 所有核心引导文件
2. context/ 系统文件
3. .agent/skills/_shared/ - 通用框架
4. 当前使用的 skills 和 workflows

---

## 快速清理命令（可选）

删除临时脚本：

```powershell
del find_today_changes.py
del scan_project_files.py
```

删除特定 skill（示例）：

```powershell
rmdir /s /q .agent\skills\docker-lint
rmdir /s /q .agent\skills\k8s-lint
```

删除特定 workflow（示例）：

```powershell
del .agent\workflows\bmad-*.md  # 删除所有 bmad- 开头的
```

---

## 估算节省空间

- 临时脚本: ~10 KB
- 10 个未使用 skills: ~200-300 KB
- 30 个未使用 workflows: ~150-200 KB

__总计可节省__: 约 400-500 KB（对于 36K+ 行项目来说很小）

---

## 结论

本项目整体很干净，没有发现典型的垃圾文件（缓存、日志等）。

__主要优化方向__：

1. 根据实际使用删除不需要的 workflows
2. 根据技术栈删除不需要的 skills
3. 删除临时分析脚本

__不建议大规模清理__，因为：

- 这些文件都是有目的的（框架、工具、文档）
- 占用空间很小
- 可能在将来需要
