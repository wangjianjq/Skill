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
if exist PROJECT_STATUS.md (
    del /f /q PROJECT_STATUS.md
    echo [OK] Removed PROJECT_STATUS.md
)
if exist sprint-status.yaml (
    del /f /q sprint-status.yaml
    echo [OK] Removed sprint-status.yaml
)
if exist USER_PROFILE.md (
    del /f /q USER_PROFILE.md
    echo [OK] Removed USER_PROFILE.md
)
if exist .ag_env_verified (
    del /f /q /a .ag_env_verified
    echo [OK] Invalidated environment verification
)
if exist .git (
    echo.
    echo [WARNING] This will permanently delete the .git directory and all Git history!
    set /p confirm_git="Are you sure? (y/N): "
    if /i "%confirm_git%"=="y" (
        rmdir /s /q .git
        echo [OK] Removed .git directory (for clean distribution)
    ) else (
        echo [SKIP] .git directory preserved.
    )
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
echo [NEXT STEP] To re-initialize the project, run:
echo     setup.bat
echo.
echo Or manually edit PROJECT_STATUS.md to set your governance mode.
echo.
echo [INFO] After initialization, you can start working with the AI.
echo ========================================================
echo.
pause

