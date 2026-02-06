# Python Format - PowerShell Script
param(
    [string]$Path = ".",
    [switch]$Check = $false,
    [switch]$Verbose = $false
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "🎨 Python Format - 正在格式化代码..." -ForegroundColor Cyan
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

# 检查 Black
try {
    $blackVersion = black --version 2>&1
    if ($LASTEXITCODE -ne 0) { throw }
    Write-Host "✅ Black: $blackVersion" -ForegroundColor Green
}
catch {
    Write-Host "⚠️  警告: 未检测到 Black" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "📥 正在尝试安装 Black..." -ForegroundColor Cyan
    
    try {
        pip install black --quiet
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Black 安装成功!" -ForegroundColor Green
            $blackVersion = black --version 2>&1
            Write-Host "   版本: $blackVersion" -ForegroundColor Green
        }
        else {
            throw
        }
    }
    catch {
        Write-Host "❌ 自动安装失败，请手动安装:" -ForegroundColor Red
        Write-Host "   pip install black" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "💡 或使用 pipx 安装全局版本（推荐）:" -ForegroundColor Cyan
        Write-Host "   pipx install black" -ForegroundColor Cyan
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

# 构建 Black 命令
$blackArgs = @($targetPath)

if ($Check) {
    $blackArgs += "--check"
    Write-Host "🔍 检查模式: 仅检查不修改" -ForegroundColor Yellow
    Write-Host ""
}

if ($Verbose) {
    $blackArgs += "--verbose"
}

# 执行格式化
Write-Host "🚀 开始执行..." -ForegroundColor Green
Write-Host ""

& black @blackArgs

$exitCode = $LASTEXITCODE

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

# 输出结果
if ($exitCode -eq 0) {
    if ($Check) {
        Write-Host "✅ 格式检查通过: 未发现问题!" -ForegroundColor Green
    } else {
        Write-Host "✅ 格式化完成!" -ForegroundColor Green
    }
}
else {
    if ($Check) {
        Write-Host "⚠️  格式检查失败: 发现代码风格问题" -ForegroundColor Yellow
        Write-Host "   请运行不带 -Check 参数的命令以自动修复" -ForegroundColor DarkGray
    } else {
        Write-Host "❌ 格式化过程中出现错误" -ForegroundColor Red
    }
}

Write-Host ""
exit $exitCode
