# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-07 ~14:30 UTC (07/10 11:30 BRT). Mes corrente: 2026-10.
# Filtro de tipo: issuetype in ("Epic","Fluxo de trabalho").
# 6 conjuntos do mes corrente reconsultados ao vivo + getVisibleJiraProjects
# (21 projetos, total=21, isLast=true). pageInfo.hasNextPage=false nas 6 consultas.
# 'planned' estourou o limite de tokens e foi reduzido via jq no arquivo salvo
# pelo runtime; hash canonico ao vivo a5f2cc04a74ddb4b1e0db447 == _snap/planned_2026-10.json.
# ALTERACAO: overdue ganhou EG0240-4 (TOMO V - PRE, EG0240/GOITA, duedate 2026-09-10,
# statusCategory indeterminate, updated 2026-10-07T10:38:24.040-0300). A issue foi
# reaberta/alterada hoje as 10:38 BRT e passou a contar como atrasada. 2 -> 3 itens.
# Demais conjuntos (planned/lookahead/sent/resolved/rework) sem alteracao.
# ARTIFACT_HTML (C:\Users\DELL\Documents\Claude\Artifacts\pr03-relatorio-indicadores-epics\
# index.html) segue inacessivel a sessao Cowork (protected location). Geracao usou
# _artifact_src.html, a copia local versionada no repo.
import json, os, hashlib
D = os.path.dirname(os.path.abspath(__file__))
K = '2026-10'

def it(key, summary, stname, stcat, pkey, pname, due, res, upd):
    return {"key": key, "fields": {"summary": summary,
            "status": {"name": stname, "statusCategory": {"key": stcat}},
            "project": {"key": pkey, "name": pname},
            "duedate": due, "resolutiondate": res, "updated": upd}}

LIVE = {}
LIVE['overdue'] = [
 it('EG0239-28','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)','Em Revisão','indeterminate','EG0239','EG0239 - CARPINA/ COMPESA','2026-08-10',None,'2026-09-21T10:55:55.586-0300'),
 it('EG0240-4','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)','Em Revisão','indeterminate','EG0240','EG0240 - GOITÁ/ COMPESA','2026-09-10',None,'2026-10-07T10:38:24.040-0300'),
 it('EG0240-5','TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)','Em Revisão','indeterminate','EG0240','EG0240 - GOITÁ/ COMPESA','2026-09-30',None,'2026-09-21T10:07:17.904-0300'),
]
P_DNIT   = ('EG0286','EG0286 - DNIT/AC ')
P_EMB    = ('EG0285','EG0285 - EMBASA - BARREIRAS')
P_ART    = ('EG0294','EG0294 - ARTLOT - Topografia')
P_274    = ('EG0274','EG0274 - DNIT')
P_280    = ('G0280','EG0280 - DMAE')
P_241    = ('EG0241','EG0241 - XARÉU/ COMPESA')
P_275    = ('EG0275','EG0275 - CODEVASF')
P_240    = ('EG0240','EG0240 - GOITÁ/ COMPESA')
P_239    = ('EG0239','EG0239 - CARPINA/ COMPESA')
PEND = ('Tarefas pendentes','new'); REV = ('Em Revisão','indeterminate'); AND_ = ('Em andamento','indeterminate')
def mk(k, s, st, p, due, upd): return it(k, s, st[0], st[1], p[0], p[1], due, None, upd)
LIVE['lookahead'] = [
 mk('EG0286-19','Projeto de contenções (pb)',PEND,P_DNIT,'2026-11-03','2026-06-17T17:38:40.836-0300'),
 mk('EG0285-16','RELATÓRIO DOS IMPACTOS SOCIAIS (RIS) ',PEND,P_EMB,'2026-11-03','2026-05-14T11:31:20.526-0300'),
 mk('EG0285-8','ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)',REV,P_EMB,'2026-11-03','2026-09-30T11:46:00.212-0300'),
 mk('EG0285-18','SERVIÇOS GEOTÉCNICOS',PEND,P_EMB,'2026-11-09','2026-05-14T11:31:30.030-0300'),
 mk('EG0285-14','RELATÓRIO GEOTÉCNICO ',PEND,P_EMB,'2026-11-09','2026-05-14T11:31:11.610-0300'),
 mk('EG0294-3','São Roque',PEND,P_ART,'2026-11-18','2026-10-02T13:45:46.124-0300'),
 mk('EG0294-2','Navegantes/Artlot',PEND,P_ART,'2026-11-18','2026-10-02T13:45:37.682-0300'),
 mk('EG0294-1','Baía/Artlot',PEND,P_ART,'2026-11-18','2026-10-02T13:45:29.242-0300'),
 mk('EG0286-6','Estudo de traçado',PEND,P_DNIT,'2026-11-18','2026-09-30T11:08:02.268-0300'),
 mk('EG0274-66','Proj. Básico - Orçamento e Plano de Execução da Obra',PEND,P_274,'2026-11-18','2026-05-28T17:47:05.587-0300'),
 mk('EG0274-65','Proj. Básico - Projeto de Desapropriação',PEND,P_274,'2026-11-18','2026-05-28T17:47:08.171-0300'),
 mk('G0280-75','Administração e Coordenação do Contrato',AND_,P_280,'2026-11-30','2026-09-30T11:29:49.398-0300'),
 mk('EG0274-57','Proj. Básico - Projeto Geométrico e Interseções',PEND,P_274,'2026-11-30','2026-08-20T17:04:14.132-0300'),
 mk('EG0241-45','Administração e Coordenação do Contrato',PEND,P_241,'2026-11-30','2026-09-21T14:45:40.371-0300'),
 mk('EG0286-18','Projeto de obras de arte especiais (pb)',PEND,P_DNIT,'2026-12-03','2026-06-17T17:38:36.976-0300'),
 mk('EG0286-14','Projeto geométrico e de interseções (pb)',PEND,P_DNIT,'2026-12-09','2026-09-30T11:08:32.515-0300'),
 mk('EG0286-24','Orçamento e plano de execução de obra (pb)',PEND,P_DNIT,'2026-12-16','2026-06-17T17:39:06.103-0300'),
 mk('EG0286-9','Estudo geotécnico de subleito/ e ocorrências',PEND,P_DNIT,'2026-12-30','2026-09-30T11:08:11.622-0300'),
 mk('EG0275-108','Administração e Coordenação do Contrato',AND_,P_275,'2026-12-31','2026-05-05T09:21:58.639-0300'),
 mk('EG0240-44','Administração e Coordenação do Contrato',AND_,P_240,'2026-12-31','2026-05-05T09:21:36.085-0300'),
 mk('EG0239-54','Administração e Coordenação do Contrato',AND_,P_239,'2026-12-31','2026-05-11T16:20:36.026-0300'),
]
ENV = ('Enviado - Aguardando Análise','done')
S286 = it('EG0286-7','Estudo de tráfego',ENV[0],ENV[1],P_DNIT[0],P_DNIT[1],'2026-10-01','2026-10-02T13:40:01.911-0300','2026-10-02T13:40:01.929-0300')
S275 = it('EG0275-112','Licenças Ambientais',ENV[0],ENV[1],P_275[0],P_275[1],'2026-09-04','2026-10-02T09:27:36.092-0300','2026-10-02T09:27:36.111-0300')
S241 = it('EG0241-42','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)',ENV[0],ENV[1],P_241[0],P_241[1],'2026-09-10','2026-10-02T09:30:29.370-0300','2026-10-02T09:30:46.892-0300')
LIVE['sent']     = [S286, S275, S241]
LIVE['resolved'] = [S286, S275, S241]
LIVE['rework']   = [S286, S241]

def canon(d):
    return hashlib.sha256(json.dumps(sorted(d,key=lambda x:x['key']),sort_keys=True,
           ensure_ascii=False,separators=(',',':')).encode()).hexdigest()[:24]

print('--- diff vs rodada anterior (_run1007b, 10:30 BRT 07/10) ---')
mudou = []
for name, data in LIVE.items():
    p = os.path.join(D, '%s_%s.json' % (name, K))
    old = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else []
    if canon(old) == canon(data):
        print('%-10s sem alteracao (%d itens)' % (name, len(data)))
        continue
    ok, nk = {i['key'] for i in old}, {i['key'] for i in data}
    print('%-10s ALTERADO %d->%d  +%s  -%s' % (name, len(old), len(data),
          sorted(nk-ok) or '-', sorted(ok-nk) or '-'))
    json.dump(data, open(p,'w',encoding='utf-8'), ensure_ascii=False, separators=(',',':'))
    mudou.append(name)
print('planned    hash ao vivo a5f2cc04a74ddb4b1e0db447 vs arquivo %s'
      % canon(json.load(open(os.path.join(D,'planned_%s.json'%K),encoding='utf-8'))))
print('RESULTADO: alterados -> %s' % (', '.join(mudou) or 'nenhum'))
