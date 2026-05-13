# =====================================================================
# install-task.ps1
# Cria (ou recria) a tarefa agendada do Windows que roda auto-push.ps1
# a cada 30 minutos, como o usuario atual, sem precisar de senha.
# Rode UMA VEZ para instalar. Nao precisa ser admin.
# =====================================================================

$taskName   = 'PR03-Auto-Push-GitHub'
$repoPath   = 'C:\Users\DELL\Documents\Claude\pr03-relatorio-publico'
$scriptPath = Join-Path $repoPath 'auto-push.ps1'

if (-not (Test-Path $scriptPath)) {
    Write-Host "ERRO: nao encontrei $scriptPath" -ForegroundColor Red
    Write-Host "Verifique se o auto-push.ps1 existe na pasta do repo."
    exit 1
}

# Remove tarefa antiga, se existir
$existing = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "Removendo tarefa antiga..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
}

# Acao: rodar PowerShell em modo silencioso passando o script
$action = New-ScheduledTaskAction `
    -Execute 'powershell.exe' `
    -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$scriptPath`"" `
    -WorkingDirectory $repoPath

# Gatilho: a cada 30 minutos, comecando 1 minuto a partir de agora,
# repetindo "para sempre" (na pratica: por 9999 dias)
$startAt = (Get-Date).AddMinutes(1)
$trigger = New-ScheduledTaskTrigger `
    -Once -At $startAt `
    -RepetitionInterval (New-TimeSpan -Minutes 30) `
    -RepetitionDuration (New-TimeSpan -Days 9999)

# Configuracoes: nao parar na bateria, esperar PC ligar, limite 5 min
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 5) `
    -MultipleInstances IgnoreNew

# Principal: roda como o usuario logado, sem privilegio elevado
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
    -Description "Empurra para GitHub os snapshots do PR03 gerados pelo Cowork. Roda a cada 30 min." | Out-Null

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "  Tarefa criada com sucesso!" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Nome:        $taskName"
Write-Host "  Script:      $scriptPath"
Write-Host "  Frequencia:  a cada 30 minutos (proximo: $startAt)"
Write-Host "  Log:         $repoPath\.auto-push.log"
Write-Host ""
Write-Host "Rodando uma vez agora pra testar..." -ForegroundColor Cyan
Start-ScheduledTask -TaskName $taskName
Start-Sleep -Seconds 5

Write-Host ""
Write-Host "Ultimas linhas do log:" -ForegroundColor Cyan
Write-Host "----------------------------------------"
if (Test-Path "$repoPath\.auto-push.log") {
    Get-Content "$repoPath\.auto-push.log" -Tail 15
} else {
    Write-Host "(log ainda nao gerado - aguarde mais alguns segundos e rode 'Get-Content $repoPath\.auto-push.log -Tail 15')"
}
Write-Host "----------------------------------------"
Write-Host ""
Write-Host "Pronto! Daqui pra frente o GitHub sera atualizado automaticamente." -ForegroundColor Green
Write-Host "Pra ver/desabilitar a tarefa: abra o Task Scheduler (taskschd.msc)."
