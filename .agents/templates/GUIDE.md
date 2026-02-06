# Template Usage Guide / 模板使用指南

> **Location**: `.agents/templates/`  
> **Purpose**: 本目录包含所有协议文件的标准模板，确保项目中新增规范文件的结构一致性

---

## 📐 Available Templates / 可用模板

### 1. LANG_TEMPLATE.md - 语言协议模板

**用途**: 创建新的编程语言规范文件  
**文件名格式**: `LANG_{LANGUAGE_NAME}.md`  
**示例**: `LANG_RUBY.md`, `LANG_PHP.md`, `LANG_DART.md`

**必需内容**:

- ✅ `## Schema: Language Specification` 元数据区块
- ✅ Modern Stack 和 Legacy Stack 区分
- ✅ Best Practices 最佳实践
- ✅ Critical Rules 关键规则

---

### 2. SKILL_TEMPLATE.md - 技能协议模板

**用途**: 创建新的技能门禁或流程规范  
**文件名格式**: `SKILL_{SKILL_NAME}.md`  
**示例**: `SKILL_SECURITY.md`, `SKILL_PERFORMANCE.md`

**必需内容**:

- ✅ `## Schema: Skill Definition` 元数据区块
- ✅ Activation Protocol 激活协议
- ✅ Technical Implementation Standards 技术实现标准
- ✅ Verification 验证要求

---

### 3. FW_TEMPLATE.md - 框架协议模板

**用途**: 创建新的框架或技术栈规范  
**文件名格式**: `FW_{FRAMEWORK_NAME}.md`  
**示例**: `FW_DJANGO.md`, `FW_ANGULAR.md`

**必需内容**:

- ✅ `## Schema: Framework Specification` 元数据区块
- ✅ Project Initialization 项目初始化
- ✅ Architecture 架构模式
- ✅ Development Workflow 开发工作流

---

## 🤖 AI Agent Enforcement / AI 强制执行机制

### 强制性规则来源

模板使用由以下协议文件强制执行：

1. **[AGENTS.md](file:///c:/Users/WJ/Desktop/Skill/AGENTS.md)** (第 29-46 行)
   - 规则 #6: **Template Enforcement (Structural Consistency)**
   - 要求所有新协议文件必须使用对应模板
   - 要求所有新协议文件必须包含 `## Schema:` 区块

2. **[PROJECT_GOVERNANCE.md](file:///c:/Users/WJ/Desktop/Skill/PROJECT_GOVERNANCE.md)** (第 51-64 行)
   - Step 3 Implementation 阶段的 **Template Compliance** 规则
   - 明确列出三种模板的使用场景

### 执行机制

当 AI Agent 需要创建新的协议文件时：

```
IF (file type is Language OR Skill OR Framework protocol)
THEN
    1. 读取对应模板文件
    2. 复制模板结构
    3. 填充实际内容（替换占位符）
    4. 验证 Schema 区块存在
    5. 保存到正确路径
ELSE
    按常规方式创建文件
END IF
```

---

## 📝 Usage Examples / 使用示例

### 示例 1: 创建新语言协议

**场景**: 用户请求添加 Ruby 语言支持

**AI 操作流程**:

1. 读取 `.agents/templates/LANG_TEMPLATE.md`
2. 创建 `.agents/lang/LANG_RUBY.md`
3. 替换模板占位符:

   ```markdown
   ## Schema: Language Specification
   - language: Ruby
   - category: scripting_language
   - latest_supported_version: 3.3+
   - package_manager: bundler
   - ...
   ```

4. 填充 Modern/Legacy Stack, Best Practices 等章节
5. 更新 `AGENTS.md` 的知识索引

---

### 示例 2: 创建新技能协议

**场景**: 添加安全审计技能

**AI 操作流程**:

1. 读取 `.agents/templates/SKILL_TEMPLATE.md`
2. 创建 `.agents/skills/SKILL_SECURITY_AUDIT.md`
3. 定义 Schema:

   ```markdown
   ## Schema: Skill Definition
   - skill_id: security_audit
   - skill_category: security
   - activation_trigger: auto
   - enforcement_level: mandatory
   ```

4. 定义激活条件和实施标准

---

### 示例 3: 创建新框架协议

**场景**: 添加 Django 框架支持

**AI 操作流程**:

1. 读取 `.agents/templates/FW_TEMPLATE.md`
2. 创建 `.agents/frameworks/FW_DJANGO.md`
3. 定义 Schema:

   ```markdown
   ## Schema: Framework Specification
   - framework: Django
   - category: web
   - language: Python
   - latest_supported_version: 5.0+
   ```

4. 填充项目初始化、架构模式等章节

---

## ⚠️ Common Mistakes to Avoid / 常见错误

### ❌ 错误 1: 忘记添加 Schema 区块

```markdown
# Language: NewLang

## Environment
...
```

**问题**: 缺少 `## Schema:` 元数据区块

**修复**:

```markdown
# Language: NewLang

## Schema: Language Specification
- language: NewLang
- category: ...
- ...

---

## Environment
...
```

---

### ❌ 错误 2: Schema 字段不完整

```markdown
## Schema: Language Specification
- language: NewLang
```

**问题**: Schema 字段太少，缺少关键元数据

**修复**: 参考现有 `LANG_*.md` 文件，确保至少包含:

- `language`
- `category`
- `latest_supported_version`
- `package_manager` (如适用)
- `type_system`

---

### ❌ 错误 3: 直接创建文件而不使用模板

**问题**: 未遵循模板，导致结构不一致

**修复**: 严格按照模板创建，确保:

1. Schema 区块在顶部
2. 章节结构与模板一致
3. 使用水平线 `---` 分隔 Schema 和正文

---

## 🔄 Template Evolution / 模板演进

### 模板更新流程

当需要改进模板时：

1. **提案阶段**: 在 `.agents/sandbox/` 创建提案文件
2. **讨论阶段**: 与用户确认模板改进方案
3. **批准阶段**: 用户确认后更新模板文件
4. **迁移阶段**: 可选择性地将现有文件迁移到新模板结构

### 版本控制

- 模板文件本身不包含版本号
- 通过 Git commit history 追踪模板变更
- CHANGELOG.md 记录重大模板变更

---

## 📚 Related Documents / 相关文档

- [AGENTS.md](file:///c:/Users/WJ/Desktop/Skill/AGENTS.md) - AI Agent 核心协议
- [PROJECT_GOVERNANCE.md](file:///c:/Users/WJ/Desktop/Skill/PROJECT_GOVERNANCE.md) - 项目治理规范
- [CHANGELOG.md](file:///c:/Users/WJ/Desktop/Skill/CHANGELOG.md) - 变更日志

---

## ✅ Checklist for New Protocol Files / 新协议文件检查清单

创建新协议文件时，请确认：

- [ ] 已阅读对应模板文件
- [ ] 文件名符合命名规范 (`LANG_*.md` / `SKILL_*.md` / `FW_*.md`)
- [ ] 包含完整的 `## Schema:` 元数据区块
- [ ] Schema 字段与模板一致（或合理扩展）
- [ ] 章节结构遵循模板
- [ ] 使用 `---` 分隔 Schema 和正文
- [ ] 更新 `AGENTS.md` 知识索引（如需要）
- [ ] 更新 `CHANGELOG.md` 记录新增文件

---

**Last Updated**: 2026-02-03  
**Enforced By**: AGENTS.md (Rule #6), PROJECT_GOVERNANCE.md (Step 3)
