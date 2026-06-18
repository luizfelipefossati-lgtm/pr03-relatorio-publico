# =====================================================================
# watch-and-push.ps1  (v2)
# Vigia o working tree do repo PR03 em tempo real. Quando o Cowork
# (re)gera o snapshot e ESCREVE o index.html / README.md, detecta na
# hora e roda auto-push.ps1 (que limpa lock + commita + pusha).
# Assim o site atualiza em segundos, sem esperar a tarefa de 30 min.
# Roda como daemon em background, iniciado no logon do Windows.
# =====================================================================

$ErrorActionPreference = 'Continue'
$RepoPath  = 'C:\Users\DELL\Documents\Claude\pr03-relatorio-publico'
$AutoPush  = Join-Path $RepoPath 'auto-push.ps1'
$LogPath   = Join-Path $RepoPath '.watch.log'

# Arquivos do working tree cuja mudanca deve disparar o push.
# (NAO reagimos a .auto-push.log / .watch.log para evitar loop.)
$TriggerFiles = @('index.html', 'README.md')

function Log($msg) {
    $stamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    "$stamp  $msg" | Add-Content -Path $LogPath -Encoding UTF8
}

if (Test-Path $LogPath) {
    if ((Get-Item $LogPath).Length -gt 1MB) {
        Move-Item $LogPath "$LogPath.old" -Force -ErrorAction SilentlyContinue
    }
}

Log "=== Watcher v2 iniciado. Vigiando index.html/README.md em $RepoPath ==="

# Estado de debounce compartilhado com os handlers de evento
$global:PR03_lastTrigger = [DateTime]::MinValue

function Invoke-AutoPush {
    $now = Get-Date
    if (($now - $global:PR03_lastTrigger).TotalSeconds -lt 8) { return }  # debounce
    $global:PR03_lastTrigger = $now

    Log "Mudanca no snapshot detectada. Aguardando 3s para a escrita terminar..."
    Start-Sleep -Seconds 3
    try {
        & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $AutoPush 2>&1 |
            ForEach-Object { Log "  push: $_" }
        Log "auto-push concluido."
    } catch {
        Log "ERRO ao chamar auto-push: $_"
    }
}

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $RepoPath
$watcher.Filter = '*'                 # filtramos por nome no handler
$watcher.IncludeSubdirectories = $false
$watcher.NotifyFilter = [System.IO.NotifyFilters]::LastWrite -bor `
                        [System.IO.NotifyFilters]::FileName -bor `
                        [System.IO.NotifyFilters]::Size
$watcher.EnableRaisingEvents = $true

# MessageData carrega a lista de arquivos-gatilho para dentro do handler
$action = {
    $name = $Event.SourceEventArgs.Name
    if ($Event.MessageData -contains $name) {
        Invoke-AutoPush
    }
}

Register-ObjectEvent -InputObject $watcher -EventName 'Changed' -SourceIdentifier 'PR03Changed' -MessageData $TriggerFiles -Action $action | Out-Null
Register-ObjectEvent -InputObject $watcher -EventName 'Created' -SourceIdentifier 'PR03Created' -MessageData $TriggerFiles -Action $action | Out-Null
Register-ObjectEvent -InputObject $watcher -EventName 'Renamed' -SourceIdentifier 'PR03Renamed' -MessageData $TriggerFiles -Action $action | Out-Null

Log "Eventos registrados (Changed/Created/Renamed). Aguardando mudancas..."

try {
    while ($true) {
        Start-Sleep -Seconds 3600
        Log "(heartbeat - watcher ativo)"
    }
} finally {
    Unregister-Event -SourceIdentifier 'PR03Changed' -ErrorAction SilentlyContinue
    Unregister-Event -SourceIdentifier 'PR03Created' -ErrorAction SilentlyContinue
    Unregister-Event -SourceIdentifier 'PR03Renamed' -ErrorAction SilentlyContinue
    $watcher.Dispose()
    Log "=== Watcher encerrado ==="
}
