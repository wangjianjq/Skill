# JavaScript Lint - PowerShell Script
param([string]$Path = ".", [switch]$Fix = $false, [string]$Extensions = "js,jsx,ts,tsx")
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Write-Host "🔍 JavaScript Lint - ESLint" -ForegroundColor Cyan
Write-Host ""

# 检查 Node.js 和 ESLint
try {
    node --version | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Node not found" }
} catch {
    Write-Host "❌ Node.js 未安装: https://nodejs.org" -ForegroundColor Red
    exit 1
}

try {
    eslint --version | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "ESLint not found" }
} catch {
    Write-Host "⚠️  正在安装 ESLint..." -ForegroundColor Yellow
    npm install -g eslint
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ 请手动安装: npm install -g eslint" -ForegroundColor Red
        exit 1
    }
}

$args = @($Path, "--ext", $Extensions)
if ($Fix) { $args += "--fix" }
& eslint @args
exit $LASTEXITCODE
