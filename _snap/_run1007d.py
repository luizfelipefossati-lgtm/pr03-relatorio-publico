# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-07 ~15:30 UTC (07/10 12:30 BRT). Mes corrente: 2026-10.
# Filtro: issuetype in ("Epic","Fluxo de trabalho"). pageInfo.hasNextPage=false em todas.
# getVisibleJiraProjects: total=21, isLast=true.
# ARTIFACT_HTML (Artifacts\pr03-relatorio-indicadores-epics\index.html) continua
# inacessivel (protected location); o HTML ao vivo foi obtido via artifact staging
# (list_legacy_live_artifacts + device_stage_files artifact_ids) e conferido contra
# _artifact_src.html, a copia versionada usada na geracao.
import json, os, hashlib
D = os.path.expanduser('~/mnt/pr03-relatorio-publico/_snap')
K = '2026-10'

PN = {p['key']: p['name'] for p in json.load(open(os.path.join(D, os.pardir, '_projects_min.json'), encoding='utf-8'))}

def it(key, summary, stname, stcat, pkey, due, res, upd):
    return {"key": key, "fields": {"summary": summary,
            "status": {"name": stname, "statusCategory": {"key": stcat}},
            "project": {"key": pkey, "name": PN.get(pkey, pkey)},
            "duedate": due, "resolutiondate": res, "updated": upd}}

PEND, REV, AND_, ENV = ('Tarefas pendentes','new'), ('Em Revisão','indeterminate'), ('Em andamento','indeterminate'), ('Enviado - Aguardando Análise','done')

LIVE = {}
LIVE['overdue'] = [
 it('EG0239-28','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)',*REV,'EG0239','2026-08-10',None,'2026-09-21T10:55:55.586-0300'),
 it('EG0240-4','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)',*REV,'EG0240','2026-09-10',None,'2026-10-07T10:38:24.040-0300'),
 it('EG0240-5','TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)',*REV,'EG0240','2026-09-30',None,'2026-09-21T10:07:17.904-0300'),
]
LIVE['lookahead'] = [
 it('EG0286-19','Projeto de contenções (pb)',*PEND,'EG0286','2026-11-03',None,'2026-06-17T17:38:40.836-0300'),
 it('EG0285-16','RELATÓRIO DOS IMPACTOS SOCIAIS (RIS) ',*PEND,'EG0285','2026-11-03',None,'2026-05-14T11:31:20.526-0300'),
 it('EG0285-8','ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)',*REV,'EG0285','2026-11-03',None,'2026-09-30T11:46:00.212-0300'),
 it('EG0285-18','SERVIÇOS GEOTÉCNICOS',*PEND,'EG0285','2026-11-09',None,'2026-05-14T11:31:30.030-0300'),
 it('EG0285-14','RELATÓRIO GEOTÉCNICO ',*PEND,'EG0285','2026-11-09',None,'2026-05-14T11:31:11.610-0300'),
 it('EG0294-3','São Roque',*PEND,'EG0294','2026-11-18',None,'2026-10-02T13:45:46.124-0300'),
 it('EG0294-2','Navegantes/Artlot',*PEND,'EG0294','2026-11-18',None,'2026-10-02T13:45:37.682-0300'),
 it('EG0294-1','Baía/Artlot',*PEND,'EG0294','2026-11-18',None,'2026-10-02T13:45:29.242-0300'),
 it('EG0286-6','Estudo de traçado',*PEND,'EG0286','2026-11-18',None,'2026-09-30T11:08:02.268-0300'),
 it('EG0274-66','Proj. Básico - Orçamento e Plano de Execução da Obra',*PEND,'EG0274','2026-11-18',None,'2026-05-28T17:47:05.587-0300'),
 it('EG0274-65','Proj. Básico - Projeto de Desapropriação',*PEND,'EG0274','2026-11-18',None,'2026-05-28T17:47:08.171-0300'),
 it('G0280-75','Administração e Coordenação do Contrato',*AND_,'G0280','2026-11-30',None,'2026-09-30T11:29:49.398-0300'),
 it('EG0274-57','Proj. Básico - Projeto Geométrico e Interseções',*PEND,'EG0274','2026-11-30',None,'2026-08-20T17:04:14.132-0300'),
 it('EG0241-45','Administração e Coordenação do Contrato',*PEND,'EG0241','2026-11-30',None,'2026-09-21T14:45:40.371-0300'),
 it('EG0286-18','Projeto de obras de arte especiais (pb)',*PEND,'EG0286','2026-12-03',None,'2026-06-17T17:38:36.976-0300'),
 it('EG0286-14','Projeto geométrico e de interseções (pb)',*PEND,'EG0286','2026-12-09',None,'2026-09-30T11:08:32.515-0300'),
 it('EG0286-24','Orçamento e plano de execução de obra (pb)',*PEND,'EG0286','2026-12-16',None,'2026-06-17T17:39:06.103-0300'),
 it('EG0286-9','Estudo geotécnico de subleito/ e ocorrências',*PEND,'EG0286','2026-12-30',None,'2026-09-30T11:08:11.622-0300'),
 it('EG0275-108','Administração e Coordenação do Contrato',*AND_,'EG0275','2026-12-31',None,'2026-05-05T09:21:58.639-0300'),
 it('EG0240-44','Administração e Coordenação do Contrato',*AND_,'EG0240','2026-12-31',None,'2026-05-05T09:21:36.085-0300'),
 it('EG0239-54','Administração e Coordenação do Contrato',*AND_,'EG0239','2026-12-31',None,'2026-05-11T16:20:36.026-0300'),
]
LIVE['sent'] = [
 it('EG0286-7','Estudo de tráfego',*ENV,'EG0286','2026-10-01','2026-10-02T13:40:01.911-0300','2026-10-02T13:40:01.929-0300'),
 it('EG0275-112','Licenças Ambientais',*ENV,'EG0275','2026-09-04','2026-10-02T09:27:36.092-0300','2026-10-02T09:27:36.111-0300'),
 it('EG0241-42','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)',*ENV,'EG0241','2026-09-10','2026-10-02T09:30:29.370-0300','2026-10-02T09:30:46.892-0300'),
]
LIVE['resolved'] = list(LIVE['sent'])
LIVE['rework'] = [LIVE['sent'][0], LIVE['sent'][2]]

def canon(items):
    return hashlib.sha256(json.dumps(sorted(items, key=lambda i: i['key']), sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()[:24]

for name, items in LIVE.items():
    p = os.path.join(D, '%s_%s.json' % (name, K))
    old = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None
    ho, hn = (canon(old) if old is not None else '-'), canon(items)
    print('%-10s %2d itens  old=%s new=%s %s' % (name, len(items), ho, hn, 'IGUAL' if ho == hn else '*** ALTERADO ***'))
    json.dump(items, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))

# planned: arquivo gerado no container via jq
pn = os.path.join(D, 'planned_%s.json.new' % K)
po = os.path.join(D, 'planned_%s.json' % K)
new = json.load(open(pn, encoding='utf-8'))
old = json.load(open(po, encoding='utf-8'))
print('%-10s %2d itens  old=%s new=%s %s' % ('planned', len(new), canon(old), canon(new), 'IGUAL' if canon(old) == canon(new) else '*** ALTERADO ***'))
# normaliza nomes de projeto pelo _projects_min.json (mesma regra do _conv.py)
for i in new:
    i['fields']['project']['name'] = PN.get(i['fields']['project']['key'], i['fields']['project']['name'])
json.dump(new, open(po, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
os.rename(pn, os.path.join(os.path.expanduser('~'), 'planned_consumed.json'))
print('OK datasets gravados')
