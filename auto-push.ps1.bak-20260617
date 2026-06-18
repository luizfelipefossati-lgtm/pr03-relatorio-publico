# =====================================================================
# auto-push.ps1
# Empurra para o GitHub qualquer snapshot novo gerado pelo Cowork.
# Roda autonomamente via Task Scheduler do Windows (a cada 30 min).
# Idempotente: se nao tem nada novo, sai sem fazer nada.
# =====================================================================

# Continue (nao Stop): mensagens de git no stderr (ex: "From https://...")
# nao devem virar erro fatal. Tratamos falhas via $LASTEXITCODE manualmente.
$ErrorActionPreference = 'Continue'
$RepoPath = 'C:\Users\DELL\Documents\Claude\pr03-relatorio-publico'
$LogPath  = Join-Path $RepoPath '.auto-push.log'

function Log($msg) {
    $stamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    "$stamp  $msg" | Add-Content -Path $LogPath -Encoding UTF8
}

# Roda o log se passar de 1 MB (mantem so o ultimo)
if (Test-Path $LogPath) {
    if ((Get-Item $LogPath).Length -gt 1MB) {
        Move-Item $LogPath "$LogPath.old" -Force
    }
}

Log "=== Iniciando auto-push ==="

try {
    Set-Location $RepoPath

    # Confere se o git esta instalado
    $null = Get-Command git -ErrorAction Stop

    # Recupera de .git/index corrompido (acontece as vezes com OneDrive/AV)
    $gitStatus = & git status --porcelain 2>&1
    if ($LASTEXITCODE -ne 0 -and ($gitStatus -match 'index file corrupt' -or $gitStatus -match 'bad signature')) {
        Log "Index corrompido. Regenerando..."
        Remove-Item .git\index -Force -ErrorAction SilentlyContinue
        & git read-tree HEAD 2>&1 | Out-Null
        $gitStatus = & git status --porcelain 2>&1
    }
    if ($LASTEXITCODE -ne 0) {
        Log "git status falhou: $gitStatus"
        exit 1
    }

    $hasLocalChanges = [bool]$gitStatus

    # Pega estado do remoto
    & git fetch origin main 2>&1 | Out-Null
    $unpushed = & git log origin/main..HEAD --oneline 2>&1
    $hasUnpushedCommits = [bool]$unpushed

    if (-not $hasLocalChanges -and -not $hasUnpushedCommits) {
        Log "Nada para fazer. Saindo."
        exit 0
    }

    if ($hasLocalChanges) {
        Log "Mudancas locais detectadas:"
        $gitStatus | ForEach-Object { Log "  $_" }

        & git add -A 2>&1 | Out-Null
        $commitMsg = "Auto-push PR03 snapshot " + (Get-Date -Format 'yyyy-MM-ddTHH:mm:ssZ')
        $commitOut = & git -c user.name="PR03 Auto-Push" -c user.email="felipe.fossati@engeplus.eng.br" commit -m $commitMsg 2>&1
        Log "commit: $commitOut"
    }

    Log "Empurrando para origin/main..."
    $pushOut = & git push origin main 2>&1
    $pushExit = $LASTEXITCODE

    # Se foi rejeitado por estar atras do remoto, faz rebase e tenta de novo
    if ($pushExit -ne 0 -and ($pushOut -match 'non-fast-forward' -or $pushOut -match 'rejected')) {
        Log "Push rejeitado (atras do remoto). Tentando rebase..."
        $pullOut = & git pull --rebase --autostash origin main 2>&1
        Log "pull: $pullOut"
        if ($LASTEXITCODE -eq 0) {
            $pushOut = & git push origin main 2>&1
            $pushExit = $LASTEXITCODE
        }
    }

    if ($pushExit -eq 0) {
        Log "Push OK"
        Log "=== Concluido com sucesso ==="
        exit 0
    } else {
        Log "Push falhou (exit $pushExit): $pushOut"
        exit 1
    }
} catch {
    Log "ERRO inesperado: $_"
    exit 1
}
