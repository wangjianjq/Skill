# SKILL_ONBOARDING.md

> **Purpose**: Conduct a one-time "Handshake Interview" with the user to establish their Developer Persona.
> **Trigger**: Automatically triggered by `AGENTS.md` if `USER_PROFILE.md` is missing.
> **Flow**: Entry Point -> Step 1 -> Step 2 -> Step 3 -> Step 4 (Tools) -> Generate Profile.

## 1. 🎤 The Friendly Opening (Mandatory Script)

You **MUST** output the following message exactly as your FIRST response when this skill is activated. Do not summarize it.

**👋 Welcome / 欢迎**

**EN**: This is your first time using our "Development Specifications" environment, also known as the development "Constitution". Before you begin, we need to get to know each other to see what strategy I should use to better serve your current status. Please co-operate with me on this.

Please answer my questions truthfully. This conversation is **one-time only** ⚠️ and will not disturb you in the future. Rest assured, my understanding of you after this conversation will be limited to the local file `USER_PROFILE.md`.

**ZH**: 您这是第一次使用AI“我们的开发规范”开发环境也就是所谓的开发“宪法”。在您使用前我们需要互相了解一下，看看我应该用什么样的策略更好的针对您的现状进行服务，请您无论如何配合我的工作。

也请您一定要真实的回答我的提问，这次对话是 **一次性的** ⚠️，今后不会再打扰到您，而且您可以放心，本次对话后我对您的了解将限定在本地文件 `USER_PROFILE.md` 中。

**EN**: Shall we begin?
(**⚠️ Rule**: If you reply in **English** (e.g., "Yes" or "OK"), I will conduct the interview in **English**. If you reply in **Chinese** (e.g., "好的"), I will switch to **Chinese**.)

**ZH**: 我们现在开始吧？
(**⚠️ 规则**：如果您用**英文**回复（如 "Yes"或"OK"），我将用**英文**访谈。如果您用**中文**回复（如 "好的"），我将切换为**中文**。**🚩 请慎重选择您的回复语言！**)

## 2. ⏭️ Start the Loop

After the user replies to the welcome message:

1. **Detect Language**: Set the session language based on their reply.
2. **Trigger Step 1**: Immediately read and execute `.agents/skills/user-onboarding/step_01_experience.md`.
