@echo off
:: [AGENTS-MD] Protocol Reset Tool (ResetAG)
:: Purpose: Unlock the project and force re-initialization WITHOUT deleting the framework.

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
