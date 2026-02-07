# JavaScript Format - PowerShell Script  
param([string]$Path = ".", [switch]$Check = $false, [string]$Extensions = "js,jsx,ts,tsx,json,css,md")
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Write-Host "🎨 JavaScript Format - Prettier" -ForegroundColor Cyan
Write-Host ""

try {
    node --version | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Node not found" }
} catch {
    Write-Host "❌ Node.js 未安装: https://nodejs.org" -ForegroundColor Red
    exit 1
}

try {
    prettier --version | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Prettier not found" }
} catch {
    Write-Host "⚠️  正在安装 Prettier..." -ForegroundColor Yellow
    npm install -g prettier
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ 请手动安装: npm install -g prettier" -ForegroundColor Red
        exit 1
    }
}

$pattern = $Extensions -replace ',', ','
$args = @("--write", "$Path/**/*.{$pattern}")
if ($Check) { $args = @("--check", "$Path/**/*.{$pattern}") }
& prettier @args
exit $LASTEXITCODE
