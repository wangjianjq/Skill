# Step 4: Tooling & Governance Injection

> **Purpose**: Identify AI environment to perform "God Mode" injection.
> **Next Step**: End of Onboarding. Generate `USER_PROFILE.md`.

## 🗣️ The Question

**Instructions**:
Ask the following question in the chosen language.

**EN**:
"Final question to set up your environment: Which AI tool are you primarily using right now?
1. **Cursor**
2. **Windsurf / Codeium**
3. **VS Code + Cline / Roo Code**
4. **Google Antigravity**
5. **Claude Code (CLI)**
6. **Other**
(I will use this to configure the 'God Mode' governance injection for you.)"

**ZH**:
“最后一个问题来配置环境：您当前主要使用哪个 AI 工具？
1. **Cursor**
2. **Windsurf / Codeium**
3. **VS Code + Cline / Roo Code**
4. **Google Antigravity**
5. **Claude Code (CLI)**
6. **其他**
（我将根据您的选择为您配置‘上帝模式’的治理注入，防止我以后‘失忆’。）”

## ⏭️ Action

After user replies:

1. **Execute Injection**: Read `.agents/skills/GOD_MODE.md` and perform the injection for the selected tool immediately.
2. **Generate** the `USER_PROFILE.md` file based on all answers.

## 💾 Generating the Profile (CRITICAL)

Once the user answers this final question, you **MUST** generate a file named `USER_PROFILE.md` in the project root.

**Template**:

```markdown
# USER_PROFILE.md

## 👤 Developer Persona
- **Global Experience**: [Extracted from Step 1]
- **Interaction Style**: [Extracted from Step 3]
- **Preferred AI Tool**: [Extracted from Step 4]

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
"Thank you! Your profile has been saved to `USER_PROFILE.md`. I have also configured the 'God Mode' injection for your tool. I am now ready to assist you."

**ZH**:
"谢谢！您的画像已保存至 `USER_PROFILE.md`。我已为您配置了‘上帝模式’防注入机制。今后我会按照目前的记录为您服务。现在让我们愉快的开始创作吧。"
