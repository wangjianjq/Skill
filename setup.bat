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

REM Install dependencies from requirements.txt
if exist requirements.txt (
    echo [AGENTS-MD] Installing dependencies from requirements.txt...
    where uv >nul 2>nul
    if %ERRORLEVEL% EQU 0 (
        uv pip install -r requirements.txt
    ) else (
        pip install -r requirements.txt
    )
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
    echo   [1] Frozen      - Strict version control, no upgrades
    echo   [2] Progressive - Balance stability and innovation (Recommended)
    echo   [3] Aggressive  - Proactive modernization
    echo.
    set "mode=2"
    set /p mode="Enter your choice (1/2/3) [Default: 2]: "
    
    if "%mode%"=="1" (
        echo.
        echo [AGENTS-MD] Creating PROJECT_STATUS.md with Frozen mode...
        call :create_status Frozen
    ) else if "%mode%"=="2" (
        echo.
        echo [AGENTS-MD] Creating PROJECT_STATUS.md with Progressive mode...
        call :create_status Progressive
    ) else if "%mode%"=="3" (
        echo.
        echo [AGENTS-MD] Creating PROJECT_STATUS.md with Aggressive mode...
        call :create_status Aggressive
    ) else (
        echo.
        echo [WARNING] Invalid choice. Defaulting to Progressive mode...
        call :create_status Progressive
    )
    echo.
)

echo [AGENTS-MD] Setup Complete. Agent Environment is ready for Passive Context.
goto :end

:create_status
set "mode_desc=Keep old files, write new code via protocol. / 保留旧文件，新代码遵循协议规范。"
if /i "%~1"=="Frozen" set "mode_desc=Strict version control, no upgrades. / 严格保持现有依赖版本，不做任何升级。"
if /i "%~1"=="Aggressive" set "mode_desc=Proactive modernization and refactoring. / 主动提议现代化重构和依赖升级。"

(
    echo # PROJECT_STATUS.md
    echo.
    echo ## Schema: Project Status
    echo.
    echo - document_type: project_status_tracking
    echo - governance_mode: %~1
    echo - target_audience: ai_agents
    echo - enforcement_level: mandatory
    echo - last_updated: %date%
    echo - compatible_with: Agents-MD Pro v8.0
    echo.
    echo ---
    echo.
    echo ## Governance Mode / 治理模式
    echo.
    echo **Mode**: %~1 ✅
    echo.
    echo **Description**: 
    echo %mode_desc%
    echo.
    echo ---
    echo.
    echo ## Project Skeleton / 项目结构
    echo.
    echo Skill/
    echo ├── .agents/             # Protocol Land ^(Immutable Core Rules^)
    echo ├── scripts/             # Core Utilities ^& Configuration
    echo ├── bmad/                # BMAD Method workflows
    echo ├── context/             # Memory and status
    echo ├── docs/                # Documentation
    echo ├── AGENTS_INDEX.yaml    # Knowledge Index
    echo ├── *.md                 # Master boot and AI adapters
    echo ├── *.py                 # Root-level utility scripts
    echo └── setup.bat/sh         # Environment setup
    echo \`\`\`
    echo.
    echo ---
    echo.
    echo ## Tech Stack / 技术栈
    echo.
    echo - **Languages**: Python ^(utility scripts^)
    echo - **Protocols**: Agents-MD Pro v8.0, BMAD Method
    echo - **Supported Languages**: zh-CN, en
    echo.
    echo ---
    echo.
    echo ## Architectural Decisions / 架构决策
    echo.
    echo ^| ADR ^| Title ^| Status ^|
    echo ^|-----^|-------^|--------^|
    echo ^| ADR-001 ^| 混合智能架构 ^| ✅ Active ^|
    echo ^| ADR-002 ^| 禁用 Eval ^| ✅ Active ^|
    echo ^| ADR-003 ^| 认知镜像协议 ^| ✅ Active ^|
    echo.
    echo ---
    echo.
    echo ## Technical Debt / 技术债务
    echo.
    echo - [ ] None recorded yet
    echo.
    echo ---
    echo.
    echo ## Design Audit Status / 设计审计状态
    echo.
    echo - **Status**: Not Started
    echo - **Last Audit**: N/A
    echo.
    echo ---
    echo.
    echo ## LastTask / 最近任务
    echo.
    echo ^| Field ^| Value ^|
    echo ^|-------^|-------^|
    echo ^| Task ^| Project Initialization ^|
    echo ^| Status ^| ✅ Completed ^|
    echo ^| Date ^| %date% ^|
    echo.
    echo ---
    echo.
    echo ## Changelog / 变更日志
    echo.
    echo ### %date%
    echo - chore: Project initialized with %~1 mode via setup script.
) > PROJECT_STATUS.md
echo [OK] PROJECT_STATUS.md created with %~1 mode
goto :eof

:end

