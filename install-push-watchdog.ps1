# =====================================================================
# install-push-watchdog.ps1
# Cria (ou recria) a tarefa agendada do Windows "PR03-Push-Watchdog"
# que roda pr03-push-watchdog.ps1 a cada 10 minutos, como o usuario
# atual, sem senha e sem privilegio elevado.
# Rode UMA VEZ para instalar. Nao precisa ser admin.
# =====================================================================

$taskName   = 'PR03-Push-Watchdog'
$repoPath   = 'C:\Users\DELL\Documents\Claude\pr03-relatorio-publico'
$scriptPath = Join-Path $repoPath 'pr03-push-watchdog.ps1'
$intervalMin = 10   # cadencia do watchdog (min)

if (-not (Test-Path $scriptPath)) {
    Write-Host "ERRO: nao encontrei $scriptPath" -ForegroundColor Red
    exit 1
}

# Remove tarefa antiga, se existir
$existing = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "Removendo tarefa antiga..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
}

$action = New-ScheduledTaskAction `
    -Execute 'powershell.exe' `
    -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$scriptPath`"" `
    -WorkingDirectory $repoPath

# Gatilho: a cada N min, comecando 2 min a partir de agora,
# defasado da tarefa de 30 min para reduzir chance de corrida
$startAt = (Get-Date).AddMinutes(2)
$trigger = New-ScheduledTaskTrigger `
    -Once -At $startAt `
    -RepetitionInterval (New-TimeSpan -Minutes $intervalMin) `
    -RepetitionDuration (New-TimeSpan -Days 9999)

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 5) `
    -MultipleInstances IgnoreNew

$principal = New-ScheduledTaskPrincipal `
    -UserId "$env:USERDOMAIN\$env:USERNAME" `
    -LogonType Interactive `
    -RunLevel Limited

Register-ScheduledTask `
    -TaskName    $taskName `
    -Action      $action `
    -Trigger     $trigger `
    -Settings    $settings `
    -Principal   $principal `
    -Description "Watchdog: verifica se o snapshot PR03 chegou ao GitHub e, se lock travar ou push falhar, corrige e empurra sozinho. Roda a cada $intervalMin min." | Out-Null

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "  Watchdog instalado com sucesso!" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Nome:        $taskName"
Write-Host "  Script:      $scriptPath"
Write-Host "  Frequencia:  a cada $intervalMin minutos (proximo: $startAt)"
Write-Host "  Log:         $repoPath\.push-watchdog.log"
Write-Host ""
Write-Host "Rodando uma vez agora pra testar (isso ja deve empurrar o snapshot pendente)..." -ForegroundColor Cyan
Start-ScheduledTask -TaskName $taskName
Start-Sleep -Seconds 8

Write-Host ""
Write-Host "Ultimas linhas do log:" -ForegroundColor Cyan
Write-Host "----------------------------------------"
if (Test-Path "$repoPath\.push-watchdog.log") {
    Get-Content "$repoPath\.push-watchdog.log" -Tail 20
} else {
    Write-Host "(log ainda nao gerado - rode 'Get-Content $repoPath\.push-watchdog.log -Tail 20' em alguns segundos)"
}
Write-Host "----------------------------------------"
Write-Host ""
Write-Host "Pronto. Quando o lock travar, o watchdog resolve sozinho em ate $intervalMin min." -ForegroundColor Green
Write-Host "Ver/desabilitar: Task Scheduler (taskschd.msc) -> $taskName"
