@echo off
:: [AGENTS-MD] Protocol Reset Tool (ResetAG)
:: Purpose: Unlock the project and force re-initialization WITHOUT deleting the framework.

:: Enable UTF-8 for Chinese characters
chcp 65001 >nul

echo ========================================================
echo   AGENTS-MD PROTOCOL RESET TOOL (v7.5 Refined)
echo ========================================================
echo.
echo [!] WARNING: This will reset project-specific configurations.
echo     Core framework directories (bmad, .agents) are preserved.
echo.

:: 1. Remove governance and status markers
echo [1/3] Clearing state markers...
:: PROJECT_STATUS.md and USER_PROFILE.md are mandatory.
:: We reset them to a CLEAN state instead of deleting them.
:: PROJECT_STATUS.md is mandatory. Initialize with clean template.
(
    echo # PROJECT_STATUS.md
    echo.
    echo ## Governance Mode / 治理模式
    echo Progressive / 渐进式
    echo.
    echo ## Project Skeleton / 项目骨架
    echo ^(To be populated by AI on first run / 待 AI 首次运行时填充^)
    echo.
    echo ## Tech Stack / 技术栈
    echo []
    echo.
    echo ## Architectural Decisions / 架构决策
    echo []
    echo.
    echo ## Technical Debt / 技术债务
    echo []
    echo.
    echo ## Design Audit Status / 设计审计状态
    echo []
    echo.
    echo ## Last Task / 上次任务
    echo [None / 无]
) > PROJECT_STATUS.md
echo [OK] Initialized PROJECT_STATUS.md (Template)
:: USER_PROFILE.md is mandatory. Initialize with clean template.
(
    echo # USER_PROFILE.md
    echo.
    echo ## User Preferences / 用户偏好
    echo.
    echo - **Communication Language / 沟通语言**: [Select: Chinese / English]
    echo - **Role / 角色**: [Select: Developer / Architect / CTO]
    echo.
    echo ## Persona Handshake / 角色握手
    echo.
    echo ^(To be populated during onboarding / 待入职期间填充^)
) > USER_PROFILE.md
echo [OK] Initialized USER_PROFILE.md (Template)
if exist sprint-status.yaml (
    del /f /q sprint-status.yaml
    echo [OK] Removed sprint-status.yaml
)
if exist .ag_env_verified (
    del /f /q /a .ag_env_verified
    echo [OK] Invalidated environment verification
)

:: ---------------------------------------------------------
:: [NEW] Section: Context Factory Reset
:: ---------------------------------------------------------
echo [Reset] Cleaning up Context Memory...

if exist context (
    rmdir /s /q context
    echo [OK] Deleted existing context
)
mkdir context

:: Restore context\memory.md (Core ADRs)
(
    echo # 决策记忆库 ^(TOC^)
    echo.
    echo 1. [ADR-001] 架构转型: 混合智能
    echo 2. [ADR-002] 安全审计: 禁用 Eval
    echo 3. [ADR-003] 语言协议: 认知镜像
    echo.
    echo ## [ADR-001] 架构转型: 混合智能
    echo.
    echo - 决定: 采用 "Passive Context (Brain) + Active Skills (Hands)" 架构。
    echo - 原因: Vercel 研究证明被动上下文对知识检索最有效，而 Skils 对执行具体动作（如 formatting）最稳定。
    echo.
    echo ## [ADR-002] 安全审计: 禁用 Eval
    echo.
    echo - 决定: 全局禁用 shell 脚本中的 `eval`，改用数组扩展。
    echo - 原因: 2026-02-05 安全审计发现潜在注入风险 (lint.sh^)。
    echo.
    echo ## [ADR-003] 语言协议: 认知镜像
    echo.
    echo - 决定: 实施 "Cognitive Mirroring Protocol"，强制 AI 用此匹配用户对话语言。
    echo - 原因: 用户要求元认知工件 ^(Task/Plan^) 必须本地化，以提升协作体验。
) > context\memory.md
echo [OK] Restored context\memory.md (Factory Default)

:: Restore context\status.md (Project Meta)
(
    echo ^<project_meta^>
    echo.
    echo - 当前阶段: Agents-MD Pro v7.5 Ultimate 维护与审计阶段。
    echo - 核心架构: 被动上下文 (Passive Context) + 混合智能 (Hybrid Intelligence)。
    echo - 技术栈: Python, PowerShell, Bash, Markdown (AgentsProtocols).
    echo - 核心原则:
    echo     1. 认知镜像协议 (Cognitive Mirroring Protocol): AI 输出语言必须匹配用户语言。
    echo     2. 认知漏斗 (Cognitive Funnel): 强制引导所有 AI 读取 AGENTS.md。
    echo ^</project_meta^>
) > context\status.md
echo [OK] Restored context\status.md (Factory Default)

:: ---------------------------------------------------------
:: [INFO] .gemini directory contains project config (settings.json) and is preserved.
:: ---------------------------------------------------------

:: 2. Clear project-specific configurations
echo [2/3] Resetting configurations...
if exist bmad\bmm\config.yaml (
    del /f /q bmad\bmm\config.yaml
    echo [OK] Reset BMAD BMM config
)
if exist bmad\core\config.yaml (
    del /f /q bmad\core\config.yaml
    echo [OK] Reset BMAD Core config
)
if exist _bmad-output (
    rmdir /s /q _bmad-output
    echo [OK] Cleaned up runtime output directory
)

:: 3. Forced Context Logic
echo [3/3] Forcing protocol re-indexing...
if exist AGENTS.md (
    copy /b AGENTS.md +,, >nul
    echo [OK] Updated AGENTS.md timestamp
)

:: 4. Distribution Mode (Optional)
echo.
set /p dist_mode="[?] Prepare for new distribution? (Reset CHANGELOG history) (y/N): "
if /i "%dist_mode%"=="y" (
    echo [4/4] Resetting CHANGELOG.md...
    if exist CHANGELOG.md (
        del /f /q CHANGELOG.md
        echo [OK] Deleted old CHANGELOG
    )
    (
        echo # CHANGELOG
        echo.
        echo ## Project Initialized
        echo.
        echo - chore: Project initialized for distribution.
    ) > CHANGELOG.md
    echo [OK] Created fresh CHANGELOG.md
)


echo.
echo ========================================================
echo [SUCCESS] Project state reset.
echo.
echo [ACTION REQUIRED] Please copy and paste the following to the AI:
echo.
echo "Protocol Reset. Read AGENTS.md to re-initialize."
echo ========================================================
echo.
pause
