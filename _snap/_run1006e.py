# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-06 ~15:30 UTC (12:30 BRT). Mes corrente: 2026-10.
#
# ACHADO IMPORTANTE DESTA RODADA:
# O tipo de item de hierarquia 1 foi RENOMEADO no Jira de "Epic" para
# "Fluxo de trabalho" nos projetos EG0286 (DNIT/AC) e EG291 (Arroio Feijo),
# em algum momento entre 14:30 e 15:30 UTC de 2026-10-06.
# Consequencia: a JQL historica `issuetype=Epic` passou a NAO casar esses itens.
#   planned   2026-10: 29 -> 17  (perdia 12 itens)
#   lookahead 2026-10: 21 ->  9  (perdia 12 itens)
#   sent/resolved/rework: perdia EG0286-7
# Correcao aplicada nesta rodada: `issuetype in (Epic, "Fluxo de trabalho")`.
# Com o filtro corrigido, os 6 conjuntos ficaram IDENTICOS aos de _run1006d.py,
# confirmando que NAO houve mudanca real de dados - apenas a renomeacao do tipo.
#
# Observacao 2: o HTML do Live Artifact
#   C:\Users\DELL\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics\index.html
# deixou de ser legivel pela sessao Cowork (protected location). A geracao usou
# _artifact_src.html (copia local no repo), que segue valida.
import json, os
D = os.path.dirname(os.path.abspath(__file__))
K = '2026-10'

LIVE = {
 'planned': ['EG0286-7','EG0256-28','EG0274-63','EG0274-59','EG291-4','EG0274-38',
             'EG0286-21','EG0286-20','EG0286-17','EG0286-16','EG0286-15','EG0286-11',
             'EG0286-12','EG0286-23','EG0286-22','EG0274-64','EG0274-62','EG0274-61',
             'EG0274-60','G0280-54','EG0274-21','G0280-55','G0280-53','G0280-51',
             'G0280-50','EG0286-10','EG0274-58','EG0274-43','EG0256-30'],
 'overdue': ['EG0239-28','EG0240-5'],
 'lookahead': ['EG0286-19','EG0285-16','EG0285-8','EG0285-18','EG0285-14','EG0294-3',
               'EG0294-2','EG0294-1','EG0286-6','EG0274-66','EG0274-65','G0280-75',
               'EG0274-57','EG0241-45','EG0286-18','EG0286-14','EG0286-24','EG0286-9',
               'EG0275-108','EG0240-44','EG0239-54'],
 'sent': ['EG0286-7','EG0275-112','EG0241-42'],
 'resolved': ['EG0286-7','EG0275-112','EG0241-42'],
 'rework': ['EG0286-7','EG0241-42'],
}

print('--- diff vs rodada anterior (14:30 UTC, _run1006d) ---')
alterado = False
for name, keys in LIVE.items():
    p = os.path.join(D, '%s_%s.json' % (name, K))
    old = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else []
    ok = [i['key'] for i in old]
    if sorted(ok) == sorted(keys):
        print('%-10s sem alteracao (%d)' % (name, len(keys)))
    else:
        alterado = True
        print('%-10s ALTERADO %d->%d  +%s  -%s' % (name, len(ok), len(keys),
              sorted(set(keys)-set(ok)) or '-', sorted(set(ok)-set(keys)) or '-'))
print('RESULTADO:', 'HOUVE ALTERACAO - revisar' if alterado
      else 'nenhuma alteracao de dados; snapshot regerado apenas com novo timestamp')
