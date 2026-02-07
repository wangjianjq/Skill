# Step 2: The Tech Stack Matrix (The Nuance)

> **Purpose**: Identify specific strengths/weaknesses and the project's direction.
> **Next Step**: After user replies, trigger `step_03_style.md`.

## 🕵️ Context Analysis

1. **Scan** the current project's file structure.
2. **If** user source files exist (e.g., .js, .py, .cpp, .go), list them as "Detected Technologies".
3. **If** the project is empty or only contains infrastructure files (e.g., .bat, .sh, .agents/), do **NOT** assume the tech stack.

## 🗣️ The Question

**Instructions**:
Ask the following question in the user's preferred language.

**EN**:
"I noticed [Detected Tech A/B/C] in your folder. Will you be working with these, or do you have a different tech stack planned for this project?

Please list the primary technologies you'll use and rate your familiarity with each (1-5):

- **1 (Novice)**: I need step-by-step guidance for almost everything.
- **2 (Beginner)**: I can read code but struggle to write it from scratch; need help with syntax.
- **3 (Competent)**: I can write standard code but need help with best practices and complex logic.
- **4 (Proficient)**: I am very comfortable; just give me the architecture or tricky parts.
- **5 (Expert)**: I am a master; just do what I say, no explanations needed.

Also, are there any technologies you absolutely dislike?"

**ZH**:
“我注意到您的文件夹中有 [检测到的技术 A/B/C]。您打算使用这些技术，还是为该项目规划了不同的技术栈？

请列出您将使用的主要技术，并评估您对每项技术的熟悉程度（1-5）：

- **1 (新手)**: 我几乎所有事情都需要分步指导。
- **2 (初学者)**: 我能读懂代码，但在从头编写时会遇到困难；需要语法方面的帮助。
- **3 (胜任)**: 我能编写标准代码，但在最佳实践和复杂逻辑方面需要帮助。
- **4 (熟练)**: 我非常自如；只需给我架构或棘手的部分。
- **5 (专家)**: 我是大师；照我说的做，不需要解释。

另外，有什么技术是您绝对不喜欢的吗？”

## ⏭️ Action

After the user replies:

1. **Analyze** their tech stack preferences.
2. **Proceed** immediately to trigger `.agents/skills/onboarding/step_03_style.md`.
