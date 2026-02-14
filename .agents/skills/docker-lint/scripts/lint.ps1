# Docker Lint - PowerShell Script
param(
    [string]$File = "Dockerfile",
    [string]$Path = ".",
    [switch]$Recursive = $false,
    [string]$ConfigFile = ""
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "🐳 Docker Lint - 正在检查 Dockerfile..." -ForegroundColor Cyan
Write-Host ""

# 检查 hadolint 是否安装
$hadolintInstalled = $false
$useDocker = $false

try {
    $hadolintVersion = hadolint --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        $hadolintInstalled = $true
        Write-Host "✅ hadolint: $(($hadolintVersion -split '\n')[0])" -ForegroundColor Green
    }
}
catch {}

if (-not $hadolintInstalled) {
    Write-Host "⚠️  警告: hadolint 未安装在系统路径" -ForegroundColor Yellow
    
    # 检查 Docker 是否可用
    try {
        docker --version | Out-Null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Docker 可用，将使用容器运行 hadolint" -ForegroundColor Green
            $useDocker = $true
        }
    }
    catch {
        Write-Host "❌ Docker 也不可用" -ForegroundColor Red
        Write-Host ""
        Write-Host "📥 请安装 hadolint 或 Docker:" -ForegroundColor Yellow
        Write-Host "   方法1 (推荐): scoop install hadolint" -ForegroundColor Cyan
        Write-Host "   方法2: https://github.com/hadolint/hadolint/releases" -ForegroundColor Cyan
        Write-Host "   方法3: 安装 Docker Desktop" -ForegroundColor Cyan
        exit 1
    }
}

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

# 收集要检查的文件
$dockerfiles = @()

if ($Recursive) {
    $dockerfiles = Get-ChildItem -Path $Path -Filter "*Dockerfile*" -Recurse -File | Select-Object -ExpandProperty FullName
}
elseif (Test-Path $File -PathType Leaf) {
    $dockerfiles = @((Resolve-Path $File).Path)
}
else {
    $searchPath = Join-Path $Path $File
    if (Test-Path $searchPath -PathType Leaf) {
        $dockerfiles = @((Resolve-Path $searchPath).Path)
    }
    else {
        Write-Host "❌ 错误: 找不到文件: $File" -ForegroundColor Red
        exit 1
    }
}

if ($dockerfiles.Count -eq 0) {
    Write-Host "❌ 错误: 未找到任何 Dockerfile" -ForegroundColor Red
    exit 1
}

Write-Host "📁 找到 $($dockerfiles.Count) 个 Dockerfile" -ForegroundColor Cyan
Write-Host ""

$totalErrors = 0
$totalWarnings = 0

foreach ($dockerfile in $dockerfiles) {
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
    Write-Host "📄 文件: $dockerfile" -ForegroundColor Cyan
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
    Write-Host ""
    
    # 构建命令
    if ($useDocker) {
        $dockerfileDir = Split-Path $dockerfile
        $dockerfileName = Split-Path $dockerfile -Leaf
        
        $cmd = "docker run --rm -i -v `"${dockerfileDir}:/workspace`" hadolint/hadolint < /workspace/$dockerfileName"
        
        if ($ConfigFile) {
            $configDir = Split-Path $ConfigFile
            $configName = Split-Path $ConfigFile -Leaf
            $cmd = "docker run --rm -i -v `"${dockerfileDir}:/workspace`" -v `"${configDir}:/config`" hadolint/hadolint --config /config/$configName < /workspace/$dockerfileName"
        }
        
        $result = Invoke-Expression $cmd 2>&1
    }
    else {
        $args = @($dockerfile)
        if ($ConfigFile) {
            $args += "--config", $ConfigFile
        }
        
        $result = & hadolint @args 2>&1
    }
    
    if ($result) {
        Write-Host $result
        $errors = ($result | Select-String "error:").Count
        $warnings = ($result | Select-String "warning:").Count
        $totalErrors += $errors
        $totalWarnings += $warnings
    }
    else {
        Write-Host "✅ 未发现问题" -ForegroundColor Green
    }
    
    Write-Host ""
}

Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "📊 检查结果:" -ForegroundColor Cyan
Write-Host "   ❌ 错误: $totalErrors 个" -ForegroundColor $(if ($totalErrors -gt 0) { "Red" } else { "Green" })
Write-Host "   ⚠️  警告: $totalWarnings 个" -ForegroundColor $(if ($totalWarnings -gt 0) { "Yellow" } else { "Green" })
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

if ($totalErrors -gt 0) {
    Write-Host ""
    Write-Host "💡 建议查看 SKILL.md 中的 Dockerfile 修复示例" -ForegroundColor Cyan
    exit 1
}
elseif ($totalWarnings -gt 0) {
    exit 0
}
else {
    Write-Host ""
    Write-Host "✅ 所有检查通过!" -ForegroundColor Green
    exit 0
}
