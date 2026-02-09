
# Agents-MD Pro v7.5 Ultimate — AI 原生被动上下文开发框架

> **版本**: 7.5.0 Ultimate | **理念**: 零决策负担 & 被动上下文
> **最新审计**: 2026-02-02

---

## 概述

Agents-MD Pro v7.5 是一套面向 AI 辅助开发的**边界约束框架**，旨在系统性缓解大语言模型（LLM）在代码生成中常见的"幻觉"问题。通过严密的协议体系，将 AI 行为限制在可控、可预测的范围内，显著减少不可预知的错误与返工。

### ⭐ 核心价值主张

| 收益 | 描述 |
|:---|:---|
| **减少返工** | 将 AI 编程（Vibe Coding）变得可控且高效 |
| **消除误解** | 标准化规则确保用户意图被准确理解与执行 |
| **商业级交付** | 内置多语言规范、UI/UX 设计标准与自动化测试，确保专业产出 |

---

## ⭐ 项目亮点

> **Agents-MD Pro 的独特之处**

- 🔒 **协议域不可变** — 核心配置只读,防止 AI 意外破坏
- 🎤 **个性化入职访谈** — 三阶段握手问答,根据您的技能等级定制 AI 行为
- 🛡️ **双重确认安全机制** — 危险命令需精确匹配通关短语
- 📐 **50+ 框架协议** — 预验证的主流语言与框架规则 (含微信小程序、鸿蒙 HarmonyOS、React、Vue、Flutter 等)
- 🧪 **沙盒进化机制** — 新技术可在沙盒中安全测试后再正式采纳
- 🌍 **全球化优先设计** — 自动化 i18n 强制审计,支持多语言项目

---

## 核心机制与功能

### 🔍 被动上下文架构

系统使用**高密度压缩标签体系**（`AGENTS_INDEX.yaml`）自动索引项目根目录，优化"长上下文窗口"以实现最高召回精度，同时最小化 Token 消耗。

### 🤖 混合智能与 Skills 生态 (Hybrid Intelligence)

**"本地精准 + AI 推理" — 融合两极优势的最佳实践。**

Agents-MD Pro v7.5 引入了**混合使用 (Hybrid Usage)** 模式，完美融合了零成本的本地工具与强大的 AI 推理能力。本项目现已全面支持 Skills 生态系统，并支持用户根据需求自定义扩展新的 Skills。

- **自适应执行 (Adaptive Execution)**：系统智能分流任务——简单的格式化完全本地运行（0 Token），复杂的逻辑则启动 AI 推理。
- **跨 AI 可移植性 (Cross-AI Portability)**：`.agent/skills/` 中的 Skills 可被 **Antigravity, Cursor, Windsurf, Claude Code, Copilot** 等所有主流 AI 即时识别。
- **用户可扩展 (User-Extensible)**：您只需在 `.agent/skills/` 中创建新文件夹，即可轻松添加自定义 Skill。

#### 🧰 内置 Skills 矩阵

| Skill (技能) | 执行方式 | 成本 | 描述 |
|:---|:---|:---|:---|
| **format-js / python** | ⚡ 本地 | 0元 | 基于 Prettier/Black 的毫秒级代码格式化 |
| **lint-js / python** | ⚡ 本地 | 0元 | 基于 ESLint/Ruff 的静态分析与自动修复 |
| **security-check** | ⚡ 本地 | 0元 | 扫描依赖项是否存在已知漏洞 (npm/pip) |
| **run-tests** | ⚡ 本地 | 0元 | 智能识别并执行项目测试套件 |
| **git-commit** | 🧠 AI | Token | 基于约定式提交规范生成语义化提交信息 |
| **generate-changelog** | ⚡ 本地 | 0元 | 自动将 Git 历史编译为人类可读的变更日志 |

#### ⚙️ 本地工具先决条件 (Pre-requisites)

为了解锁 **零 Token 成本** 的极速体验，请确保安装以下标准工具：

- **JS/TS 开发**: `npm install -g prettier eslint`
- **Python 开发**: `pip install black ruff pip-audit`

> **注意**：若未检测到本地工具，系统将自动降级使用 AI 模拟执行（会消耗 Token）。

### 📐 规则化开发约束

内置主流开发语言与框架的**官方最新稳定版规范**，并预置经过验证的第三方框架规则，使开发者能够无缝遵循行业最佳实践。

### 🛡️ 双域安全法则（领地式访问控制）

| 领地 | 权限 | 描述 |
|:---|:---|:---|
| 🔴 **协议域** | 只读 | 核心配置（`.agents/`），AI 禁止修改或删除 |
| 🟢 **用户域** | 读写 | 所有用户项目文件，AI 拥有完全权限 |
| 🧪 **沙盒域** | 读写 | 新协议的进化区域，待用户批准后合并 |

### ⚠️ 危险动作警告法则（安全覆盖）

系统主动拦截高风险指令（如 `rm -rf /`），执行严格确认流程：

1. **双重警告**：中英文红色警告通知
2. **责任告知**：明确免责声明
3. **精确短语**：必须输入 **`I-CONFIRM`** 或 **`我已明确确认`**（不支持模糊匹配）

> 任何偏差将立即终止操作。

### 📋 轻量级开发工作流

所有 AI 辅助开发遵循此**五步流程**（定义于 `PROJECT_GOVERNANCE.md`）：

```
第1步 → 范围确认
第2步 → 迷你设计（3-7 行，鼓励双语）
第3步 → 实现（遵循 .agents/ 规则）
第4步 → 自测（逻辑验证 + 测试用例）
第5步 → 文档更新（CHANGELOG.md 必填）
```

### 🤝 个性化用户访谈

首次使用时，AI 将进行**三阶段握手访谈**以建立您的开发者画像：

| 阶段 | 目的 |
|:---|:---|
| **经验评估** | 确定整体开发水平（新手至专家） |
| **技术矩阵** | 对各项技术的熟练度进行 1-5 评分 |
| **协作风格** | 选择：互动教学 / 默实执行 / 按需讲解 |

结果存储于 `USER_PROFILE.md`，在整个项目周期为您提供定制化 AI 服务。

### 🧪 全栈多语言 QA 与测试支持

覆盖 **Python、Node.js、Go、C++、Java、移动端**等 11+ 技术栈：
- 标准化测试工作流
- 自动化单元/集成测试提醒
- 结构化日志强制规范（生产代码禁用 `print()`）

### 🎨 专业级 UI/UX 设计标准

内置**"设计闸门"**协议，强制应用现代审美：
- 玻璃态（Glassmorphism）与深度效果
- 网格布局（Bento UI）
- 专业图标库（Lucide / Heroicons）
- 4px 网格间距系统
- 暗色模式策略（CSS 变量）

### 🌍 自动化国际化（i18n）协议

强制维护 `PROJECT_LANGUAGES.md` 文件。系统自动引导多语言适配，确保功能与内容支持全球化部署。

### 🏗️ 架构治理

通过 `SKILL_ARCHITECT` 协议强制结构严谨性：
- **SOLID 原则**：强制遵守单一职责和开闭原则
- **依赖规则**：内层不得依赖外层
- **技术债务跟踪**：禁止"上帝对象"，要求明确的边界上下文
- **设计模式工具箱**：工厂、策略、观察者、适配器建议

### 📝 结构化调试规范

| 规则 | 执行 |
|:---|:---|
| **禁止** | 生产代码中使用 `print()` / `console.log()` |
| **要求** | 平台标准结构化日志，包含时间戳和级别 |
| **自动化** | 功能完成后自动提示测试 |

---

## 项目结构

### 目录树

```
Agents-MD-Pro/
├── 📄 AGENTS.md              # 主引导文件（AI 入口点）
├── 📄 AGENTS_INDEX.yaml      # 高密度压缩知识索引
├── 📄 PROJECT_GOVERNANCE.md  # 开发工作流与规则
├── 📄 CHANGELOG.md           # 自动维护的变更日志
├── 📄 README.txt             # 英文文档
├── 📄 README_zh-CN.txt       # 中文文档
│
├── 🔧 setup.bat / setup.sh   # 环境引导脚本
├── 🔧 ResetAG.bat / .sh      # 协议重置工具
├── 🔧 .cursorrules           # IDE 集成配置（包括但不限于Cursor、Antigravity、VS Code插件等IDE或各种Claude Code、Gemini CLI、OpenCode类CLI工具）
│
├── 📁 .agents/               # 🔴 协议域（只读）
│   ├── 📁 lang/              # 语言协议（C, Python, Go, Rust...）
│   ├── 📁 frameworks/        # 框架协议（React, Vue, FastAPI...）
│   ├── 📁 database/          # 数据库协议（PostgreSQL, MongoDB...）
│   ├── 📁 cloud/             # 云平台协议（AWS, GCP, Azure）
│   ├── 📁 skills/            # 技能模块（入职访谈、调试、i18n...）
│   ├── 📁 knowledge/         # 领域知识库
│   └── 📁 sandbox/           # 🧪 实验性协议沙盒
│
├── 📁 .agent/                # 工作流定义
│   └── 📁 workflows/         # 40+ BMAD 工作流脚本
│
└── 📁 bmad/                  # BMAD-Method 运行时（可选，219个文件）
```

### 文件分类

| 类别 | 文件 | 描述 |
|:---|:---|:---|
| **入口点** | `AGENTS.md` | AI 首先读取此文件，包含启动序列与核心规则 |
| **知识索引** | `AGENTS_INDEX.yaml` | 用于被动上下文检索的压缩路径映射 |
| **治理规范** | `PROJECT_GOVERNANCE.md` | 5步工作流、CHANGELOG规则、迷你设计模板 |
| **文档** | `README.txt` / `README_zh-CN.txt` | 双语项目说明文档 |
| **变更日志** | `CHANGELOG.md` | AI 自动维护的双语变更记录 |
| **环境脚本** | `setup.bat` / `setup.sh` | 安装依赖项（uv、Node.js 检测） |
| **重置工具** | `ResetAG.bat` / `ResetAG.sh` | 清除状态文件以重新初始化 |
| **IDE 集成** | `.cursorrules` | 多IDE集成规则（Cursor、Antigravity、VS Code、CLI工具等） |

### 协议目录

| 目录 | 内容 | 数量 |
|:---|:---|:---|
| `.agents/lang/` | 语言协议 | 10+ |
| `.agents/frameworks/` | 框架协议（React, Vue, FastAPI, **微信小程序**...） | 50+ |
| `.agents/database/` | 数据库协议 | 6+ |
| `.agents/cloud/` | 云平台协议 | 3+ |
| `.agents/skills/` | 技能模块（用户能力画像、调试、i18n...） | 18+ |
| `.agents/knowledge/` | 领域知识（设计、QA...） | 5+ |
| `.agents/sandbox/` | 沙盒环境实验性协议 | 为自动迭代准备 |
| `.agent/workflows/` | BMAD 工作流脚本 | 40 |
| `bmad/` | BMAD-Method 运行时 | 219 |

---

## 支持的技术栈

| 类别 | 框架 / 语言 |
|:---|:---|
| **系统级** | C, C++ (Modern), Rust, Zig |
| **后端** | Python (FastAPI/Flask), Go, Java, Node.js (TypeScript), C# (.NET Core) |
| **前端** | React (Vite/Next.js), Vue 3, Angular, TailwindCSS |
| **移动端** | Swift (iOS), Kotlin (Android), React Native, Flutter |
| **嵌入式** | Arduino, ESP-IDF, Zephyr RTOS, FreeRTOS |
| **无线调试** | BLE (nRF Sniffer), LoRa, USB 协议分析 |
| **仪器支持** | R&S CMW500, Keysight UXM 5G, Anritsu MT8821C, Tektronix 示波器, Saleae 逻辑分析仪等 |

---

## 快速开始

### 1. 部署项目

将本项目所有文件而不是解压缩的目录，全部复制到您的项目**根目录**使本项目的所有文件与子目录直接出现在您项目的根目录下。

> ⚠️ **关键**：切勿置于子目录，否则索引失效。

### 2. 环境自检（可选）

| 平台 | 命令 |
|:---|:---|
| Windows | `setup.bat` |
| Linux/macOS | `sh setup.sh` |

> 脚本会自动检查环境并安装推荐工具（如 `uv`）。若无 Node.js v20+ 环境，系统将自动降级至内置方案但性能不会大幅下降。

### 3. 选择治理模式

首次运行时（根目录无 `PROJECT_STATUS.md`），AI 将提示选择模式：

| 模式 | 描述 |
|:---|:---|
| **[1] 严格重构** | 按照 Agents-MD 协议重新组织文件 |
| **[2] 渐进式** ⭐ | 应用新规范的同时保留现有文件（推荐） |
| **[3] 保持旧制** | 沿用现有项目风格 |

> 如需重新初始化，可手动运行 `ResetAG.bat`（Windows）或 `ResetAG.sh`（Linux/macOS）。

### 4. 开始开发

AI 将自动读取 `AGENTS.md` 并加载约束规则。但是依然强烈建议您指定AI先去读取一下AGENTS.md这个文件。

---

## 注意事项

| 事项 | 描述 |
|:---|:---|
| **目录冲突保护** | 若检测到同名 `bmad` 目录，系统将使用 `_bmad` 作为运行时目录 |
| **静态资源屏蔽** | AI 默认不读取本说明文件，避免干扰 |
| **强制启动序列** | AI **必须**在处理任何开发请求前执行 Boot Sequence |
| **版本主权** | 对于存量项目，AI 读取清单文件（`package.json`、`go.mod`）选择相应协议规则 |

---

## 致谢

本项目受到以下先驱工作的启发与支持：

- **Vercel Research**（Agents.md 架构）
  提供了被动上下文的理论基础。
  [https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)

- **BMAD-METHOD**
  贡献了增强的引导与自动化规范逻辑。
  [https://github.com/bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)

---

## 延伸阅读

### 关于 BMad-Method

BMad 是一种 AI 驱动的敏捷开发框架，具备 21+ 专业代理、50+ 引导式工作流。支持 **/bmad-help** 命令获取实时指导，并设有"派对模式"允许多代理协同讨论。

### 关于 Vercel Research 的被动上下文

| 概念 | 描述 |
|:---|:---|
| **被动植入** | 将轻量索引嵌入系统提示，避免代理主动调用的决策开销 |
| **检索优先** | 引导 AI 优先参考最新文档而非训练数据 |
| **压缩索引** | 在 8KB 内实现高精度路径索引 |

---

> 通过 Agents-MD Pro v7.5，开发者可获得一个**安全、规范、高质量**的 AI 协同编码环境，显著提升从原型到交付的全程可控性与专业度。