# =====================================================================
# pr03-push-watchdog.ps1
# Watchdog do PR03: VERIFICA se o snapshot local ja chegou ao GitHub e,
# se nao chegou (lock travado, commit pendente ou push que falhou),
# corrige sozinho -> remove .git/index.lock, recupera index corrompido,
# faz add/commit/push. Assim voce nao precisa mexer manualmente quando
# o lock trava.
#
# Complementa (nao substitui) a tarefa PR03-Auto-Push-GitHub. Roda numa
# cadencia mais curta e com threshold de lock menor, para curar rapido.
#
# Instale com:  install-push-watchdog.ps1  (roda UMA vez)
# =====================================================================

$ErrorActionPreference = 'Continue'
$RepoPath      = 'C:\Users\DELL\Documents\Claude\pr03-relatorio-publico'
$LogPath       = Join-Path $RepoPath '.push-watchdog.log'
$LockMaxAgeMin = 3     # remove lock com mais de N min (evita matar commit em andamento)

function Log($msg) {
    $stamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    "$stamp  $msg" | Add-Content -Path $LogPath -Encoding UTF8
}

# Rotaciona o log se passar de 1 MB
if (Test-Path $LogPath) {
    if ((Get-Item $LogPath).Length -gt 1MB) { Move-Item $LogPath "$LogPath.old" -Force }
}

Log "=== Watchdog iniciando ==="

try {
    Set-Location $RepoPath
    $null = Get-Command git -ErrorAction Stop

    # === 1. VERIFICACAO: ja esta tudo no remoto? ===
    & git fetch origin main 2>&1 | Out-Null
    $statusProbe = & git status --porcelain 2>&1
    $indexBroken = ($LASTEXITCODE -ne 0 -and ($statusProbe -match 'index file corrupt' -or $statusProbe -match 'bad signature'))
    $unpushed    = & git log origin/main..HEAD --oneline 2>&1
    $lockPath    = Join-Path $RepoPath '.git\index.lock'
    $lockPresent = Test-Path $lockPath

    if (-not $indexBroken -and [string]::IsNullOrWhiteSpace($statusProbe) `
        -and [string]::IsNullOrWhiteSpace($unpushed) -and -not $lockPresent) {
        Log "OK: working tree limpo e remoto sincronizado. Nada a fazer."
        Log "=== Watchdog concluido (sem acao) ==="
        exit 0
    }

    Log "Pendencia detectada -> mudancas locais: '$([bool]$statusProbe)' | commits nao enviados: '$([bool]$unpushed)' | lock: '$lockPresent' | index quebrado: '$indexBroken'"

    # === 2. Remove lock orfao ===
    if ($lockPresent) {
        $lockAge = ((Get-Date) - (Get-Item $lockPath).LastWriteTime).TotalMinutes
        if ($lockAge -ge $LockMaxAgeMin) {
            Log "Lock orfao ($([math]::Round($lockAge,1)) min). Removendo..."
            Remove-Item $lockPath -Force -ErrorAction SilentlyContinue
            if (Test-Path $lockPath) { Log "ERRO: nao removeu .git/index.lock"; exit 1 }
        } else {
            Log "Lock recente ($([math]::Round($lockAge,1)) min < $LockMaxAgeMin). Pode ser commit em andamento; espero proxima execucao."
            exit 0
        }
    }

    # === 3. Recupera index corrompido ===
    if ($indexBroken) {
        Log "Index corrompido. Regenerando (rm index + read-tree HEAD)..."
        Remove-Item '.git\index' -Force -ErrorAction SilentlyContinue
        & git read-tree HEAD 2>&1 | Out-Null
    }

    # === 4. Reavalia estado apos limpeza ===
    $gitStatus = & git status --porcelain 2>&1
    if ($LASTEXITCODE -ne 0) { Log "git status ainda falha: $gitStatus"; exit 1 }
    $hasLocalChanges = [bool]$gitStatus

    # === 5. Add + commit (checando exit codes) ===
    if ($hasLocalChanges) {
        $addOut = & git add -A 2>&1
        if ($LASTEXITCODE -ne 0) { Log "ERRO: git add falhou (exit $LASTEXITCODE): $addOut"; exit 1 }

        $shaBefore = & git rev-parse HEAD 2>&1
        $msg = "Watchdog push PR03 " + (Get-Date -Format 'yyyy-MM-ddTHH:mm:ssZ')
        $commitOut = & git -c user.name="PR03 Watchdog" -c user.email="felipe.fossati@engeplus.eng.br" commit -m $msg 2>&1
        if ($LASTEXITCODE -ne 0 -and $commitOut -notmatch 'nothing to commit') {
            Log "ERRO: git commit falhou (exit $LASTEXITCODE): $commitOut"; exit 1
        }
        $shaAfter = & git rev-parse HEAD 2>&1
        if ($shaBefore -ne $shaAfter) { Log "Commit OK: $shaAfter" }
    }

    # === 6. Push com retry via rebase ===
    Log "Empurrando para origin/main..."
    $pushOut = & git push origin main 2>&1
    $pushExit = $LASTEXITCODE
    if ($pushExit -ne 0 -and ($pushOut -match 'non-fast-forward' -or $pushOut -match 'rejected')) {
        Log "Push rejeitado (atras do remoto). Rebase + retry..."
        & git pull --rebase --autostash origin main 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) { $pushOut = & git push origin main 2>&1; $pushExit = $LASTEXITCODE }
    }
    if ($pushExit -ne 0) { Log "ERRO: push falhou (exit $pushExit): $pushOut"; exit 1 }

    # === 7. VERIFICACAO FINAL: HEAD == origin/main? ===
    & git fetch origin main 2>&1 | Out-Null
    $stillUnpushed = & git log origin/main..HEAD --oneline 2>&1
    if ([string]::IsNullOrWhiteSpace($stillUnpushed)) {
        Log "Push OK e VERIFICADO: HEAD sincronizado com origin/main. Vercel deploya em ~1 min."
        Log "=== Watchdog concluido com sucesso ==="
        exit 0
    } else {
        Log "AVISO: apos push ainda ha commits nao enviados: $stillUnpushed"
        exit 1
    }
} catch {
    Log "ERRO inesperado: $_"
    exit 1
}
