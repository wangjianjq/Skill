# Step 1: Capability & Persona Assessment (能力与角色评估)

> **Goal**: Determine the user's "Capability Tier" to calibrate the AI's response strategy.

## Script

**EN**: First, I need to calibrate my "Explanation Density" based on your preference. Which of the following best describes your current state regarding this project's tech stack?

**ZH**: 首先，我需要根据您的偏好校准我的"解释密度"。关于本项目技术栈，以下哪项最符合您当前的状态？

---

### Options / 选项

**[A] 🎓 The Learner (学习者 / 学生)**
> "I am learning. Please explain concepts in detail, provide tutorials for new patterns, and teach me 'Why' and 'How'."
> "我在学习阶段。请详细解释概念，为新模式通过教程，教我'为什么'以及'怎么做'。"
> **AI Strategy**: Educator Mode (High verbosity, step-by-step).

**[B] 🔧 The Proficient (熟练者 / 熟手)**
> "I know the basics but need guidance on this specific project's agreements. Focus on best practices and architecture. Skip basic syntax explanations."
> "我懂基础，但需要针对本项目协议的指导。请关注最佳实践和架构。跳过基础语法的解释。"
> **AI Strategy**: Colleague Mode (Standard verbosity, rationale-focused).

**[C] ⚡ The Expert (专家 / 资深架构师)**
> "I am an expert. Just give me the code. Minimal explanation unless I ask. I want high-density information."
> "我是专家。直接给代码。除非我问，否则少废话。我要高密度信息。"
> **AI Strategy**: Executive Mode (Low verbosity, code-first).

---

**EN**: Please reply with **A, B, or C** (and optionally your Job Title, e.g., "B - Backend Engineer").

## ⏭️ Next Step

**Action**: Immediately read and execute `.agents/skills/user-onboarding/step_02_tech_stack.md`.
