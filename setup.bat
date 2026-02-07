@echo off
setlocal
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
    set "PATH=%USERPROFILE%\.cargo\bin;%PATH%"
)

REM Check for Node.js
node --version >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Node.js not found. BMad-Method will run in degraded mode.
    echo          Install Node.js v20+ for full functionality.
)



echo. > .ag_env_verified
if exist .ag_env_verified attrib +h .ag_env_verified
echo [AGENTS-MD] Setup Complete. Agent Environment is ready for Passive Context.
