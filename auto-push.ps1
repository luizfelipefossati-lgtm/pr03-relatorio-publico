# =====================================================================
# auto-push-v2.ps1
# Versao melhorada do auto-push.ps1 com:
#   1. Detecao + remocao automatica de .git/index.lock orfao
#   2. Verifica exit code do git add e do git commit antes de tentar push
#   3. NAO loga "Push OK" se o commit falhou
#   4. Verifica que houve commit novo antes de declarar sucesso
#
# Para instalar: substituir o auto-push.ps1 atual por este arquivo
# (a task PR03-Auto-Push-GitHub no Task Scheduler continua a mesma).
# =====================================================================

$ErrorActionPreference = 'Continue'
$RepoPath = 'C:\Users\DELL\Documents\Claude\pr03-relatorio-publico'
$LogPath  = Join-Path $RepoPath '.auto-push.log'

function Log($msg) {
    $stamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    "$stamp  $msg" | Add-Content -Path $LogPath -Encoding UTF8
}

# Rotaciona o log se passar de 1 MB
if (Test-Path $LogPath) {
    if ((Get-Item $LogPath).Length -gt 1MB) {
        Move-Item $LogPath "$LogPath.old" -Force
    }
}

Log "=== Iniciando auto-push v2 ==="

try {
    Set-Location $RepoPath
    $null = Get-Command git -ErrorAction Stop

    # === 1. Limpa .git/index.lock orfao (>10 min de idade) ===
    $lockPath = Join-Path $RepoPath '.git\index.lock'
    if (Test-Path $lockPath) {
        $lockAge = ((Get-Date) - (Get-Item $lockPath).LastWriteTime).TotalMinutes
        if ($lockAge -gt 10) {
            Log "Lock orfao detectado ($([math]::Round($lockAge,0)) min de idade). Removendo..."
            Remove-Item $lockPath -Force -ErrorAction SilentlyContinue
            if (Test-Path $lockPath) {
                Log "ERRO: nao conseguiu remover .git/index.lock"
                exit 1
            }
        } else {
            Log "Lock recente ($([math]::Round($lockAge,1)) min). Esperando proxima execucao."
            exit 0
        }
    }

    # === 2. Recupera de .git/index corrompido se necessario ===
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
    & git fetch origin main 2>&1 | Out-Null
    $unpushed = & git log origin/main..HEAD --oneline 2>&1
    $hasUnpushedCommits = [bool]$unpushed

    if (-not $hasLocalChanges -and -not $hasUnpushedCommits) {
        Log "Nada para fazer. Saindo."
        exit 0
    }

    # === 3. Add + commit, checando exit codes ===
    if ($hasLocalChanges) {
        Log "Mudancas locais detectadas:"
        $gitStatus | ForEach-Object { Log "  $_" }

        $addOut = & git add -A 2>&1
        if ($LASTEXITCODE -ne 0) {
            Log "ERRO: git add falhou (exit $LASTEXITCODE): $addOut"
            exit 1
        }

        $shaBeforeCommit = & git rev-parse HEAD 2>&1

        $commitMsg = "Auto-push PR03 snapshot " + (Get-Date -Format 'yyyy-MM-ddTHH:mm:ssZ')
        $commitOut = & git -c user.name="PR03 Auto-Push" -c user.email="felipe.fossati@engeplus.eng.br" commit -m $commitMsg 2>&1
        if ($LASTEXITCODE -ne 0) {
            # Se for so "nothing to commit" eh ok; qualquer outro erro eh fatal
            if ($commitOut -match 'nothing to commit') {
                Log "Nothing to commit (working tree limpo apos add)."
            } else {
                Log "ERRO: git commit falhou (exit $LASTEXITCODE): $commitOut"
                exit 1
            }
        } else {
            $shaAfterCommit = & git rev-parse HEAD 2>&1
            if ($shaBeforeCommit -eq $shaAfterCommit) {
                Log "AVISO: commit retornou 0 mas SHA nao mudou. Algo estranho."
            } else {
                Log "Commit OK: $shaAfterCommit"
            }
        }
    }

    # === 4. Push, checando exit code ===
    Log "Empurrando para origin/main..."
    $pushOut = & git push origin main 2>&1
    $pushExit = $LASTEXITCODE

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
        Log "Push OK. Vercel deve deployar em ~1 min."
        Log "=== Concluido com sucesso ==="
        exit 0
    } else {
        Log "ERRO: Push falhou (exit $pushExit): $pushOut"
        exit 1
    }
} catch {
    Log "ERRO inesperado: $_"
    exit 1
}
