# =====================================================================
# install-watch.ps1
# Cria tarefa do Windows que mantem watch-and-push.ps1 rodando em
# background. Inicia no logon e reinicia automaticamente se parar.
# Rode UMA VEZ para instalar. Nao precisa ser admin.
# =====================================================================

$taskName   = 'PR03-Watcher-GitHub'
$repoPath   = 'C:\Users\DELL\Documents\Claude\pr03-relatorio-publico'
$scriptPath = Join-Path $repoPath 'watch-and-push.ps1'

if (-not (Test-Path $scriptPath)) {
    Write-Host "ERRO: nao encontrei $scriptPath" -ForegroundColor Red
    exit 1
}

# Remove tarefa antiga, se existir
$existing = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "Removendo tarefa antiga..." -ForegroundColor Yellow
    Stop-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
}

# Acao: rodar PowerShell em modo invisivel com o watcher
$action = New-ScheduledTaskAction `
    -Execute 'powershell.exe' `
    -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$scriptPath`"" `
    -WorkingDirectory $repoPath

# Gatilho: ao logar no Windows (suficiente para uso pessoal,
# nao precisa de admin como o -AtStartup precisaria)
$triggers = @(
    (New-ScheduledTaskTrigger -AtLogOn -User "$env:USERDOMAIN\$env:USERNAME")
)

# Configuracoes: reinicia automatico, sem limite de tempo, prioriza bateria
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Days 0) `
    -RestartCount 999 `
    -RestartInterval (New-TimeSpan -Minutes 1) `
    -MultipleInstances IgnoreNew

# Principal: roda como usuario logado, sem privilegio elevado
$principal = New-ScheduledTaskPrincipal `
    -UserId "$env:USERDOMAIN\$env:USERNAME" `
    -LogonType Interactive `
    -RunLevel Limited

Register-ScheduledTask `
    -TaskName    $taskName `
    -Action      $action `
    -Trigger     $triggers `
    -Settings    $settings `
    -Principal   $principal `
    -Description "Vigia o repo PR03. Quando o Cowork comita (via Run now ou cron 6h), pusha pro GitHub imediatamente (~3s)." | Out-Null

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "  Watcher instalado com sucesso!" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Nome:        $taskName"
Write-Host "  Script:      $scriptPath"
Write-Host "  Gatilho:     no logon do Windows e ao ligar o PC"
Write-Host "  Log:         $repoPath\.watch.log"
Write-Host ""
Write-Host "Iniciando agora..." -ForegroundColor Cyan
Start-ScheduledTask -TaskName $taskName
Start-Sleep -Seconds 4

Write-Host ""
Write-Host "Ultimas linhas do log do watcher:" -ForegroundColor Cyan
Write-Host "----------------------------------------"
if (Test-Path "$repoPath\.watch.log") {
    Get-Content "$repoPath\.watch.log" -Tail 10
} else {
    Write-Host "(log ainda nao gerado - aguarde alguns segundos)"
}
Write-Host "----------------------------------------"
Write-Host ""
Write-Host "PRONTO! Agora quando o Cowork comitar (via Run now ou cron), o push" -ForegroundColor Green
Write-Host "acontece em ~3 segundos. Vercel atualiza em ~30s depois disso." -ForegroundColor Green
Write-Host ""
Write-Host "Pra desabilitar: abra Task Scheduler (taskschd.msc) e desabilite" -ForegroundColor Yellow
Write-Host "'$taskName'." -ForegroundColor Yellow
