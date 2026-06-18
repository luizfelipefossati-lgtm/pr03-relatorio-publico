# =====================================================================
# setup-autonomo.ps1  (rode UMA vez)
# Deixa o PR03 100% autonomo e com atualizacao NA HORA:
#   1. Remove .git/index.lock orfao e recupera index corrompido
#   2. Garante auto-push.ps1 = logica v2 (lock-clear + checagem de exit code)
#   3. Instala o WATCHER em tempo real (PR03-Watcher-GitHub):
#      assim que o Cowork gera o snapshot (escreve index.html), pusha em ~3s
#   4. Instala a tarefa de 30 min (PR03-Auto-Push-GitHub) como rede de seguranca
#   5. Dispara um push agora e mostra os logs
# Nao precisa ser admin. Nao pede senha.
# =====================================================================

$ErrorActionPreference = 'Stop'
$repoPath  = 'C:\Users\DELL\Documents\Claude\pr03-relatorio-publico'
$pushTask  = 'PR03-Auto-Push-GitHub'
$watchTask = 'PR03-Watcher-GitHub'
$pushPs1   = Join-Path $repoPath 'auto-push.ps1'
$watchPs1  = Join-Path $repoPath 'watch-and-push.ps1'
$pushLog   = Join-Path $repoPath '.auto-push.log'
$watchLog  = Join-Path $repoPath '.watch.log'
$me        = "$env:USERDOMAIN\$env:USERNAME"

Write-Host "== Setup autonomo PR03 (watcher + rede de 30 min) ==" -ForegroundColor Cyan
Set-Location $repoPath
$null = Get-Command git -ErrorAction Stop
foreach ($p in @($pushPs1, $watchPs1)) { if (-not (Test-Path $p)) { throw "Nao encontrei $p" } }

# --- 1. Trava orfa + index corrompido ---
$lockPath = Join-Path $repoPath '.git\index.lock'
if (Test-Path $lockPath) {
    Write-Host "Removendo .git\index.lock orfao..." -ForegroundColor Yellow
    Remove-Item $lockPath -Force -ErrorAction SilentlyContinue
    if (Test-Path $lockPath) { throw "Nao consegui remover $lockPath (feche qualquer git aberto e rode de novo)" }
}
& git status --porcelain *> $null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Recuperando .git\index..." -ForegroundColor Yellow
    Remove-Item (Join-Path $repoPath '.git\index') -Force -ErrorAction SilentlyContinue
    & git read-tree HEAD *> $null
}

# --- 2. Garante auto-push.ps1 = v2 ---
if ((Get-Content $pushPs1 -Raw) -notmatch 'Iniciando auto-push v2') {
    $v2 = Join-Path $repoPath 'auto-push-v2.ps1'
    if (Test-Path $v2) {
        Copy-Item $pushPs1 "$pushPs1.bak-$(Get-Date -Format yyyyMMddHHmmss)" -Force
        Copy-Item $v2 $pushPs1 -Force
        Write-Host "auto-push.ps1 atualizado para v2." -ForegroundColor Green
    } else { Write-Host "AVISO: auto-push.ps1 nao parece v2 e nao achei auto-push-v2.ps1." -ForegroundColor Yellow }
} else { Write-Host "auto-push.ps1 ja esta em v2." -ForegroundColor Green }

# --- Helper para (re)registrar tarefa ---
function Reset-Task($name) {
    $t = Get-ScheduledTask -TaskName $name -ErrorAction SilentlyContinue
    if ($t) { Stop-ScheduledTask -TaskName $name -ErrorAction SilentlyContinue; Unregister-ScheduledTask -TaskName $name -Confirm:$false }
}

# --- 3. WATCHER em tempo real (dispara push em ~3s quando o snapshot muda) ---
Reset-Task $watchTask
$wAction = New-ScheduledTaskAction -Execute 'powershell.exe' `
    -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$watchPs1`"" `
    -WorkingDirectory $repoPath
$wTrigger = New-ScheduledTaskTrigger -AtLogOn -User $me
$wSettings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
    -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Days 0) `
    -RestartCount 999 -RestartInterval (New-TimeSpan -Minutes 1) -MultipleInstances IgnoreNew
$wPrincipal = New-ScheduledTaskPrincipal -UserId $me -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName $watchTask -Action $wAction -Trigger $wTrigger `
    -Settings $wSettings -Principal $wPrincipal `
    -Description "Vigia index.html do PR03; pusha em ~3s quando o Cowork gera o snapshot." | Out-Null
Write-Host "Watcher '$watchTask' instalado." -ForegroundColor Green

# --- 4. Rede de seguranca: push a cada 30 min + no boot ---
Reset-Task $pushTask
$pAction = New-ScheduledTaskAction -Execute 'powershell.exe' `
    -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$pushPs1`"" `
    -WorkingDirectory $repoPath
$startAt = (Get-Date).AddMinutes(1)
$pTrigger30 = New-ScheduledTaskTrigger -Once -At $startAt `
    -RepetitionInterval (New-TimeSpan -Minutes 30) -RepetitionDuration (New-TimeSpan -Days 9999)
$pTriggerBoot = New-ScheduledTaskTrigger -AtStartup
$pSettings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
    -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Minutes 10) `
    -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 2) -MultipleInstances IgnoreNew
$pPrincipal = New-ScheduledTaskPrincipal -UserId $me -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName $pushTask -Action $pAction -Trigger @($pTrigger30, $pTriggerBoot) `
    -Settings $pSettings -Principal $pPrincipal `
    -Description "Push do PR03 a cada 30 min + no boot (rede de seguranca). v2: limpa lock e checa exit codes." | Out-Null
Write-Host "Rede de seguranca '$pushTask' instalada." -ForegroundColor Green

# --- 5. Liga o watcher e dispara um push agora ---
Write-Host "Iniciando watcher e disparando push imediato..." -ForegroundColor Cyan
Start-ScheduledTask -TaskName $watchTask
Start-ScheduledTask -TaskName $pushTask
Start-Sleep -Seconds 10

Write-Host "`n--- .auto-push.log (tail) ---" -ForegroundColor Cyan
if (Test-Path $pushLog) { Get-Content $pushLog -Tail 14 } else { Write-Host "(sem log ainda)" }
Write-Host "`n--- .watch.log (tail) ---" -ForegroundColor Cyan
if (Test-Path $watchLog) { Get-Content $watchLog -Tail 8 } else { Write-Host "(sem log ainda)" }
Write-Host "`nPronto. Agora: Cowork gera snapshot -> watcher pusha em ~3s -> Vercel deploya. (E a cada 30 min como backup.)" -ForegroundColor Green
