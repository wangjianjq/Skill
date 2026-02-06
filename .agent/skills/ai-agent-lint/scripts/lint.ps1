# AI Agent Lint - PowerShell Script
# 用于检查 AI Agent 项目的代码质量

param(
    [string]$Path = ".",
    [switch]$Fix = $false,
    [switch]$Verbose = $false
)

# 设置编码为 UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "🔍 AI Agent Lint - 正在检查项目..." -ForegroundColor Cyan
Write-Host ""

# 检查 Python 是否安装
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -ne 0) { throw }
    Write-Host "✅ Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ 错误: 未检测到 Python" -ForegroundColor Red
    Write-Host ""
    Write-Host "📥 请安装 Python 3.10 或更高版本:" -ForegroundColor Yellow
    Write-Host "   https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# 检查 Ruff 是否安装
try {
    $ruffVersion = ruff --version 2>&1
    if ($LASTEXITCODE -ne 0) { throw }
    Write-Host "✅ Ruff: $ruffVersion" -ForegroundColor Green
} catch {
    Write-Host "⚠️  警告: 未检测到 Ruff" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "📥 正在尝试安装 Ruff..." -ForegroundColor Cyan
    
    try {
        pip install ruff --quiet
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Ruff 安装成功!" -ForegroundColor Green
        } else {
            throw
        }
    } catch {
        Write-Host "❌ 自动安装失败，请手动安装:" -ForegroundColor Red
        Write-Host "   pip install ruff" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "💡 或使用 pipx 安装全局版本:" -ForegroundColor Cyan
        Write-Host "   pipx install ruff" -ForegroundColor Cyan
        exit 1
    }
}

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

# 解析目标路径
$targetPath = Resolve-Path -Path $Path -ErrorAction SilentlyContinue
if (-not $targetPath) {
    Write-Host "❌ 错误: 路径不存在: $Path" -ForegroundColor Red
    exit 1
}

Write-Host "📁 扫描目录: $targetPath" -ForegroundColor Cyan

# 检测项目类型
$projectType = "通用 Python 项目"
if (Test-Path "$targetPath\*langchain*" -PathType Any) {
    $projectType = "LangChain 项目"
} elseif (Test-Path "$targetPath\*autogen*" -PathType Any) {
    $projectType = "AutoGen 项目"
} elseif (Test-Path "$targetPath\*crewai*" -PathType Any) {
    $projectType = "CrewAI 项目"
}
Write-Host "📦 项目类型: $projectType" -ForegroundColor Cyan
Write-Host ""

# 构建 Ruff 命令
$ruffArgs = @("check", $targetPath)
if ($Fix) {
    $ruffArgs += "--fix"
    Write-Host "🔧 自动修复模式: 已启用" -ForegroundColor Yellow
    Write-Host ""
}
if ($Verbose) {
    $ruffArgs += "--verbose"
}

# 执行 Ruff 检查
Write-Host "🚀 开始检查..." -ForegroundColor Green
Write-Host ""

& ruff @ruffArgs

$exitCode = $LASTEXITCODE

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

# 输出结果
if ($exitCode -eq 0) {
    Write-Host "✅ 检查完成: 未发现问题!" -ForegroundColor Green
} else {
    Write-Host "⚠️  检查完成: 发现问题，请查看上方详情" -ForegroundColor Yellow
    Write-Host ""
    if (-not $Fix) {
        Write-Host "💡 提示: 使用 -Fix 参数可自动修复部分问题" -ForegroundColor Cyan
        Write-Host "   示例: .\lint.ps1 -Path . -Fix" -ForegroundColor DarkGray
    }
}

Write-Host ""
exit $exitCode
