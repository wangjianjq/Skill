# Step 3: Collaboration Style & Profile Generation

> **Purpose**: Define AI behavior and save the `USER_PROFILE.md`.
> **Final Action**: Generate profile and conclude.

## 🗣️ The Question

**Instructions**:
Ask the following question in the user's preferred language.

**EN**:
"Finally, how would you like me to explain things while coding?

[A] **Interactive Tutor (Step-by-Step)**: I will explain what I'm doing and why as I write the code. Choose this if you want to learn as we go.
[B] **Silent Pro (Code First)**: I will write the code directly with minimal explanation. I will trigger a 'Mini Design' only for complex architecture changes.
[C] **On-Demand**: I will output code by default. If you need an explanation, you will ask me.

**📌 Important Note**: Regardless of your choice, you can **ALWAYS** interrupt me to ask 'Why did you do that?' or 'Explain this part'. I will immediately switch to explanation mode for that topic."

**ZH**:
“最后，您希望我在通过代码时如何进行解释？

[A] **互动导师 (分步详解)**: 我会在编写代码时解释我在做什么以及为什么这么做。如果您想边做边学，请选择此项。
[B] **沉默专家 (代码优先)**: 我将直接编写代码，仅作最少的解释。仅在复杂的架构变更时我会触发‘迷你设计’。
[C] **按需讲解**: 默认情况下我只输出代码。如果您需要解释，请问我。

**📌 重要提示**: 无论您选择哪种方式，您**随时**可以打断我并问‘你为什么那样做？’或‘解释这一部分’。我会立即针对该主题切换到解释模式。”

## 💾 Generating the Profile (CRITICAL)

Once the user answers this final question, you **MUST** generate a file named `USER_PROFILE.md` in the project root.

**Template**:

```markdown
# USER_PROFILE.md

## 👤 Developer Persona
- **Global Experience**: [Extracted from Step 1]
- **Interaction Style**: [Extracted from Step 3]

## 🧠 Tech Matrix (Contextual Overrides)
> **Instructions for AI**: Read this matrix to adjust your behavior per file type.

| Technology | User Proficiency (1-5) | AI Strategy |
| :--- | :--- | :--- |
| [Tech A] | [Score] | [Derived Mode: Step-by-Step / Normal / Concise] |
| [Tech B] | [Score] | ... |

## 🛡️ Preference Flags
- **Detailed Explanations**: [Yes/No]
- **Privacy/Safety Level**: [Standard/High]
- **Communication Language**: [User's Language from Step 1]
```

## 🎉 Conclusion

After writing the file, confirm to the user (in their language):

**EN**:
"Thank you! Your profile has been saved to `USER_PROFILE.md`. I am now ready to assist you according to your preferences."

**ZH**:
“谢谢！您的画像已保存至 `USER_PROFILE.md`。我已初步了解到了您的情况，今后我会按照目前的记录为您服务。现在让我们愉快的开始创作吧。”
