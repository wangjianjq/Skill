# Python Lint - PowerShell Script
param(
    [string]$Path = ".",
    [switch]$Fix = $false,
    [switch]$ErrorsOnly = $false,
    [switch]$Verbose = $false
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "🐍 Python Lint - 正在检查代码..." -ForegroundColor Cyan
Write-Host ""

# 检查 Python
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -ne 0) { throw }
    Write-Host "✅ Python: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ 错误: 未检测到 Python" -ForegroundColor Red
    Write-Host ""
    Write-Host "📥 请安装 Python 3.8 或更高版本:" -ForegroundColor Yellow
    Write-Host "   https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# 检查 Ruff
try {
    $ruffVersion = ruff --version 2>&1
    if ($LASTEXITCODE -ne 0) { throw }
    Write-Host "✅ Ruff: $ruffVersion" -ForegroundColor Green
}
catch {
    Write-Host "⚠️  警告: 未检测到 Ruff" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "📥 正在尝试安装 Ruff..." -ForegroundColor Cyan
    
    try {
        pip install ruff --quiet
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Ruff 安装成功!" -ForegroundColor Green
            $ruffVersion = ruff --version 2>&1
            Write-Host "   版本: $ruffVersion" -ForegroundColor Green
        }
        else {
            throw
        }
    }
    catch {
        Write-Host "❌ 自动安装失败，请手动安装:" -ForegroundColor Red
        Write-Host "   pip install ruff" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "💡 或使用 pipx 安装全局版本（推荐）:" -ForegroundColor Cyan
        Write-Host "   pipx install ruff" -ForegroundColor Cyan
        exit 1
    }
}

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

# 解析路径
$targetPath = Resolve-Path -Path $Path -ErrorAction SilentlyContinue
if (-not $targetPath) {
    Write-Host "❌ 错误: 路径不存在: $Path" -ForegroundColor Red
    exit 1
}

Write-Host "📁 扫描目录: $targetPath" -ForegroundColor Cyan
Write-Host ""

# 构建 Ruff 命令
$ruffArgs = @("check", $targetPath)

if ($Fix) {
    $ruffArgs += "--fix"
    Write-Host "🔧 自动修复模式: 已启用" -ForegroundColor Yellow
    Write-Host ""
}

if ($ErrorsOnly) {
    $ruffArgs += "--select", "E,F"
    Write-Host "⚠️  仅显示错误（忽略警告）" -ForegroundColor Yellow
    Write-Host ""
}

if ($Verbose) {
    $ruffArgs += "--verbose"
}

# 执行检查
Write-Host "🚀 开始检查..." -ForegroundColor Green
Write-Host ""

& ruff @ruffArgs

$exitCode = $LASTEXITCODE

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

# 输出结果
if ($exitCode -eq 0) {
    Write-Host "✅ 检查完成: 未发现问题!" -ForegroundColor Green
}
else {
    Write-Host "⚠️  检查完成: 发现问题，请查看上方详情" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "💡 提示:" -ForegroundColor Cyan
    
    if (-not $Fix) {
        Write-Host "   - 使用 -Fix 参数可自动修复部分问题" -ForegroundColor DarkGray
        Write-Host "     示例: .\lint.ps1 -Fix" -ForegroundColor DarkGray
    }
    
    Write-Host "   - 使用 -ErrorsOnly 仅显示错误" -ForegroundColor DarkGray
    Write-Host "     示例: .\lint.ps1 -ErrorsOnly" -ForegroundColor DarkGray
}

Write-Host ""
exit $exitCode
