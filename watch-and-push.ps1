# =====================================================================
# watch-and-push.ps1
# Vigia o repo PR03 em tempo real. Quando o Cowork faz commit (via
# "Run now" ou execucao agendada), detecta na hora e roda auto-push.ps1.
# Roda como daemon em background, iniciado no logon do Windows.
# =====================================================================

$ErrorActionPreference = 'Continue'
$RepoPath  = 'C:\Users\DELL\Documents\Claude\pr03-relatorio-publico'
$AutoPush  = Join-Path $RepoPath 'auto-push.ps1'
$LogPath   = Join-Path $RepoPath '.watch.log'
$WatchPath = Join-Path $RepoPath '.git\refs\heads'

function Log($msg) {
    $stamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    "$stamp  $msg" | Add-Content -Path $LogPath -Encoding UTF8
}

# Roda o log se passar de 1 MB
if (Test-Path $LogPath) {
    if ((Get-Item $LogPath).Length -gt 1MB) {
        Move-Item $LogPath "$LogPath.old" -Force -ErrorAction SilentlyContinue
    }
}

Log "=== Watcher iniciado. Vigiando $WatchPath ==="

# Anti-debounce: ignora eventos disparados dentro de 5s do ultimo push
$script:lastTrigger = [DateTime]::MinValue

function Invoke-AutoPush {
    $now = Get-Date
    if (($now - $script:lastTrigger).TotalSeconds -lt 5) {
        return  # debounce
    }
    $script:lastTrigger = $now

    Log "Mudanca detectada. Aguardando 2s para git terminar..."
    Start-Sleep -Seconds 2

    try {
        & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $AutoPush 2>&1 | ForEach-Object {
            Log "  push: $_"
        }
        Log "auto-push concluido."
    } catch {
        Log "ERRO ao chamar auto-push: $_"
    }
}

# Cria o FileSystemWatcher
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $WatchPath
$watcher.Filter = '*'
$watcher.IncludeSubdirectories = $false
$watcher.NotifyFilter = [System.IO.NotifyFilters]::LastWrite -bor [System.IO.NotifyFilters]::FileName
$watcher.EnableRaisingEvents = $true

# Eventos: Changed e Created cobrem commits (que mudam refs/heads/main)
Register-ObjectEvent -InputObject $watcher -EventName 'Changed' -SourceIdentifier 'PR03Changed' -Action {
    Invoke-AutoPush
} | Out-Null

Register-ObjectEvent -InputObject $watcher -EventName 'Created' -SourceIdentifier 'PR03Created' -Action {
    Invoke-AutoPush
} | Out-Null

Log "Eventos registrados. Aguardando mudancas..."

# Heartbeat: mantem o script vivo e loga sinal de vida a cada 1h
try {
    while ($true) {
        Start-Sleep -Seconds 3600
        Log "(heartbeat - watcher ativo)"
    }
} finally {
    # Cleanup se o script for encerrado
    Unregister-Event -SourceIdentifier 'PR03Changed' -ErrorAction SilentlyContinue
    Unregister-Event -SourceIdentifier 'PR03Created' -ErrorAction SilentlyContinue
    $watcher.Dispose()
    Log "=== Watcher encerrado ==="
}
