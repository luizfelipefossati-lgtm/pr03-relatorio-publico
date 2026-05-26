# =====================================================================
# fix-vercel-deploy.ps1
# Conserta o problema do snapshot que nao subia no Vercel.
#
# CAUSA RAIZ:
#   - Em 15/05/2026 ficou um .git/index.lock orfao (0 bytes).
#   - Toda execucao do auto-push.ps1 falhava no `git commit` com
#     "Unable to create '.git/index.lock': File exists".
#   - Mas o script continuava e fazia `git push`, que retorna 0 (nada
#     pra enviar) -> logava "Push OK" sem ter realmente commitado nada.
#   - Resultado: ultimo commit real no GitHub foi 15/05/2026 ->
#     Vercel nao re-deployava ha 11 dias.
#
# COMO USAR:
#   1. Abra PowerShell na pasta pr03-relatorio-publico
#   2. Execute: .\fix-vercel-deploy.ps1
#   3. Verifique que o snapshot foi commitado e empurrado
#   4. Em ~1 min o Vercel deve fazer deploy automatico
# =====================================================================

$ErrorActionPreference = 'Stop'
$RepoPath = 'C:\Users\DELL\Documents\Claude\pr03-relatorio-publico'

Write-Host "=== Fix Vercel Deploy PR03 ===" -ForegroundColor Cyan
Set-Location $RepoPath

# 1. Remove lock orfao
$lock = Join-Path $RepoPath '.git\index.lock'
if (Test-Path $lock) {
    $lockInfo = Get-Item $lock
    $ageHours = ((Get-Date) - $lockInfo.LastWriteTime).TotalHours
    Write-Host "Encontrado .git/index.lock com $([math]::Round($ageHours,1))h de idade. Removendo..." -ForegroundColor Yellow
    Remove-Item $lock -Force
    Write-Host "  Lock removido." -ForegroundColor Green
} else {
    Write-Host "Nenhum .git/index.lock encontrado (ok)." -ForegroundColor Green
}

# 2. Mostra mudancas pendentes
Write-Host ""
Write-Host "Mudancas locais pendentes:" -ForegroundColor Cyan
git status --short

# 3. Add + commit + push
Write-Host ""
Write-Host "Fazendo commit e push..." -ForegroundColor Cyan
git add -A
if ($LASTEXITCODE -ne 0) { throw "git add falhou (exit $LASTEXITCODE)" }

$commitMsg = "Fix PR03 snapshot manual " + (Get-Date -Format 'yyyy-MM-ddTHH:mm:ssZ')
git -c user.name="PR03 Auto-Push" -c user.email="felipe.fossati@engeplus.eng.br" commit -m $commitMsg
if ($LASTEXITCODE -ne 0) {
    Write-Host "  Nada para commitar (working tree limpo)." -ForegroundColor Yellow
} else {
    Write-Host "  Commit criado." -ForegroundColor Green
}

git push origin main
if ($LASTEXITCODE -ne 0) { throw "git push falhou (exit $LASTEXITCODE)" }
Write-Host "  Push OK." -ForegroundColor Green

# 4. Verifica ultimo commit
Write-Host ""
Write-Host "Ultimo commit:" -ForegroundColor Cyan
git log -1 --oneline

Write-Host ""
Write-Host "=== Pronto! ===" -ForegroundColor Green
Write-Host "Aguarde ~1 min e verifique o deploy no Vercel."
Write-Host ""
Write-Host "PROXIMOS PASSOS:" -ForegroundColor Yellow
Write-Host "  - Substitua o auto-push.ps1 pela versao melhorada"
Write-Host "    (auto-push-v2.ps1) que detecta lock orfao automaticamente"
Write-Host "    e nao mente quando o commit falha."
