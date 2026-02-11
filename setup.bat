@echo off
setlocal

REM Ensure we run from the project root (where this script lives)
cd /d "%~dp0"

echo [AGENTS-MD] Bootstrapping Environment...

REM Check for uv
where uv >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [AGENTS-MD] 'uv' not found. Installing...
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    if %ERRORLEVEL% NEQ 0 (
        echo [ERROR] Failed to install uv. Please install manually.
        exit /b 1
    )
    set "PATH=%USERPROFILE%\.local\bin;%PATH%"
)

REM Check for Node.js
node --version >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Node.js not found. BMad-Method will run in degraded mode.
    echo          Install Node.js v20+ for full functionality.
)



echo. > .ag_env_verified
if exist .ag_env_verified attrib +h .ag_env_verified

REM Check for PROJECT_STATUS.md
if not exist PROJECT_STATUS.md (
    echo.
    echo ========================================================
    echo [AGENTS-MD] First-time setup detected.
    echo ========================================================
    echo.
    echo Please select a Governance Mode:
    echo.
    echo   [1] Frozen     - Strict version control, no upgrades
    echo   [2] Hybrid     - Balance stability and innovation (Recommended)
    echo   [3] Aggressive - Proactive modernization
    echo.
    set "mode=2"
    set /p mode="Enter your choice (1/2/3) [Default: 2]: "
    
    if "%mode%"=="1" (
        echo.
        echo [AGENTS-MD] Creating PROJECT_STATUS.md with Frozen mode...
        call :create_status Frozen
    ) else if "%mode%"=="2" (
        echo.
        echo [AGENTS-MD] Creating PROJECT_STATUS.md with Hybrid mode...
        call :create_status Hybrid
    ) else if "%mode%"=="3" (
        echo.
        echo [AGENTS-MD] Creating PROJECT_STATUS.md with Aggressive mode...
        call :create_status Aggressive
    ) else (
        echo.
        echo [WARNING] Invalid choice. Defaulting to Hybrid mode...
        call :create_status Hybrid
    )
    echo.
)

echo [AGENTS-MD] Setup Complete. Agent Environment is ready for Passive Context.
goto :end

:create_status
(
    echo # PROJECT_STATUS.md
    echo.
    echo ## ⚙️ Project Governance
    echo.
    echo ### Governance Mode
    echo.
    echo **Current Mode**: `%~1` ✅
    echo.
    echo **Mode Definitions**:
    echo.
    echo - **Frozen**: 严格保持现有依赖版本,不做任何升级
    echo - **Hybrid** ✅: 新文件使用现代标准,修改旧文件时保持原有风格
    echo - **Aggressive**: 主动提议现代化重构和依赖升级
    echo.
    echo **Selection Date**: %date%
    echo **Selected By**: User (Setup Script)
    echo.
    echo ---
    echo.
    echo ## 📋 Architectural Decision Records (ADR)
    echo.
    echo ### ADR-001: 初始化治理模式为 %~1
    echo.
    echo - **Date**: %date%
    echo - **Status**: Accepted
    echo - **Context**: 项目首次初始化,需要选择治理模式
    echo - **Decision**: 选择 %~1 模式作为治理策略
    echo.
    echo ---
    echo.
    echo ## 📝 Last Task Summary
    echo.
    echo **Task**: Project Initialization
    echo **Date**: %date%
    echo **Status**: Completed
    echo **Summary**: 环境设置完成,治理模式已选择
) > PROJECT_STATUS.md
echo [OK] PROJECT_STATUS.md created with %~1 mode
goto :eof

:end

