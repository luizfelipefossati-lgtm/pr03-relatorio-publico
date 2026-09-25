# -*- coding: utf-8 -*-
# Reconferencia ao vivo em 2026-09-25 ~15:30 UTC (12:30 BRT) - sessao agendada.
# As 6 consultas de setembro/2026 foram refeitas no Jira com
# ETQ = issuetype in ("Epic","Fluxo de trabalho"). Resultado: NENHUM DELTA
# em relacao a _run0925b.py / _verify0925b.py.
#   planned=18, overdue=2, sent=5, resolved=4, rework=2, lookahead=29
# O lookahead (2026-10-01..2026-11-30) foi executado em duas metades
# (outubro=20, novembro=9) para nao estourar o limite de tokens do MCP;
# os dois epics do EG0274 reagendados em 25/09 de manha seguem em outubro
# (EG0274-21 -> 2026-10-29, EG0274-58 -> 2026-10-30).
# getVisibleJiraProjects nao precisou ser refeito: _projects_min.json ja tem
# as 20 chaves conferidas em _verify0925b.py e nada indicou mudanca.
# Artifact: copia ao vivo obtida do desktop (device_stage_files artifact_ids=
# pr03-relatorio-indicadores-epics), md5 6a2b6462a4efbec1890af4494a7f0b74 --
# identico a _artifact_src.html.
# Este script apenas CONFERE os _snap/*.json contra os dados ao vivo; nao grava.
import json, os, sys
D = os.path.dirname(os.path.abspath(__file__))

LIVE = {
"planned_2026-09": [
 ("EG0275-112","Em Revisã","indeterminate","EG0275","2026-09-04",None,"2026-09-21T09:51:05.827-0300"),
 ("EG0275-6","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
 ("G0280-53","Tarefas pendentes","new","G0280","2026-09-08",None,"2026-07-28T16:03:46.832-0300"),
 ("EG0241-42","Em Revisão","indeterminate","EG0241","2026-09-10",None,"2026-08-31T16:44:47.690-0300"),
 ("EG0240-43","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
 ("EG0240-4","Tarefas pendentes","new","EG0240","2026-09-10",None,"2026-08-31T16:45:50.827-0300"),
 ("EG0286-13","Tarefas pendentes","new","EG0286","2026-09-14",None,"2026-07-03T11:07:40.831-0300"),
 ("G0280-51","Em andamento","indeterminate","G0280","2026-09-15",None,"2026-08-31T00:42:45.248-0300"),
 ("G0280-52","Em andamento","indeterminate","G0280","2026-09-16",None,"2026-07-28T16:05:36.102-0300"),
 ("G0280-50","Em andamento","indeterminate","G0280","2026-09-16",None,"2026-07-28T16:04:10.678-0300"),
 ("EG0285-19","Em andamento","indeterminate","EG0285","2026-09-18",None,"2026-05-18T10:57:07.064-0300"),
 ("G0280-54","Tarefas pendentes","new","G0280","2026-09-22",None,"2026-07-28T16:03:54.494-0300"),
 ("EG0286-11","Em andamento","indeterminate","EG0286","2026-09-23",None,"2026-08-30T23:27:03.793-0300"),
 ("G0280-55","Tarefas pendentes","new","G0280","2026-09-29",None,"2026-07-28T16:04:01.727-0300"),
 ("EG0286-14","Tarefas pendentes","new","EG0286","2026-09-29",None,"2026-06-17T17:38:16.515-0300"),
 ("EG0286-10","Em andamento","indeterminate","EG0286","2026-09-30",None,"2026-08-28T16:30:11.901-0300"),
 ("EG0286-6","Tarefas pendentes","new","EG0286","2026-09-30",None,"2026-08-30T23:26:14.328-0300"),
 ("EG0240-5","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
],
"overdue_2026-09": [
 ("EG0239-28","Em Revisão","indeterminate","EG0239","2026-08-10",None,"2026-09-21T10:55:55.586-0300"),
 ("EG0286-8","Em andamento","indeterminate","EG0286","2026-08-31",None,"2026-07-30T09:33:06.932-0300"),
],
"sent_2026-09": [
 ("EG0286-7","Enviado - Aguardando Análise","done","EG0286","2026-08-31","2026-09-03T16:50:04.999-0300","2026-09-03T16:50:05.010-0300"),
 ("EG0275-6","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
 ("EG0240-43","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
 ("EG0240-5","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
 ("EG0286-30","Enviado - Aguardando Análise","done","EG0286","2028-01-28","2026-09-16T10:43:24.635-0300","2026-09-16T10:43:24.656-0300"),
],
"resolved_2026-09": [
 ("EG0286-7","Enviado - Aguardando Análise","done","EG0286","2026-08-31","2026-09-03T16:50:04.999-0300","2026-09-03T16:50:05.010-0300"),
 ("EG0275-6","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
 ("EG0240-43","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
 ("EG0286-30","Enviado - Aguardando Análise","done","EG0286","2028-01-28","2026-09-16T10:43:24.635-0300","2026-09-16T10:43:24.656-0300"),
],
"rework_2026-09": [
 ("EG0240-43","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
 ("EG0240-5","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
],
"lookahead_2026-09": [
 ("G0280-75","Em andamento","indeterminate","G0280","2026-10-01",None,"2026-03-16T15:13:40.422-0300"),
 ("EG0256-28","Em andamento","indeterminate","EG0256","2026-10-01",None,"2026-04-07T13:44:09.762-0300"),
 ("EG0274-63","Tarefas pendentes","new","EG0274","2026-10-06",None,"2026-05-28T17:47:13.793-0300"),
 ("EG0274-59","Tarefas pendentes","new","EG0274","2026-10-06",None,"2026-05-28T17:47:24.997-0300"),
 ("EG0286-21","Tarefas pendentes","new","EG0286","2026-10-12",None,"2026-06-17T17:38:54.156-0300"),
 ("EG0286-20","Tarefas pendentes","new","EG0286","2026-10-12",None,"2026-06-17T17:38:44.118-0300"),
 ("EG0286-17","Tarefas pendentes","new","EG0286","2026-10-14",None,"2026-06-17T17:38:32.376-0300"),
 ("EG0286-16","Tarefas pendentes","new","EG0286","2026-10-14",None,"2026-06-17T17:38:28.787-0300"),
 ("EG0286-15","Tarefas pendentes","new","EG0286","2026-10-14",None,"2026-06-17T17:38:22.692-0300"),
 ("EG0286-12","Tarefas pendentes","new","EG0286","2026-10-19",None,"2026-09-11T12:12:51.299-0300"),
 ("EG0286-23","Tarefas pendentes","new","EG0286","2026-10-20",None,"2026-06-17T17:39:00.759-0300"),
 ("EG0286-22","Tarefas pendentes","new","EG0286","2026-10-22",None,"2026-06-17T17:38:57.611-0300"),
 ("EG0274-64","Em andamento","indeterminate","EG0274","2026-10-25",None,"2026-07-01T16:15:49.824-0300"),
 ("EG0274-62","Tarefas pendentes","new","EG0274","2026-10-25",None,"2026-05-28T17:47:16.641-0300"),
 ("EG0274-61","Tarefas pendentes","new","EG0274","2026-10-25",None,"2026-05-28T17:47:19.482-0300"),
 ("EG0274-60","Tarefas pendentes","new","EG0274","2026-10-25",None,"2026-05-28T17:47:22.404-0300"),
 ("EG0286-9","Tarefas pendentes","new","EG0286","2026-10-28",None,"2026-08-28T16:30:25.519-0300"),
 ("EG0274-21","Tarefas pendentes","new","EG0274","2026-10-29",None,"2026-09-25T09:56:37.062-0300"),
 ("EG0274-58","Tarefas pendentes","new","EG0274","2026-10-30",None,"2026-09-25T09:56:03.350-0300"),
 ("EG0256-30","Em andamento","indeterminate","EG0256","2026-10-31",None,"2026-06-03T14:39:13.026-0300"),
 ("EG0286-19","Tarefas pendentes","new","EG0286","2026-11-03",None,"2026-06-17T17:38:40.836-0300"),
 ("EG0285-16","Tarefas pendentes","new","EG0285","2026-11-03",None,"2026-05-14T11:31:20.526-0300"),
 ("EG0285-8","Enviado- Aguardando Análise","done","EG0285","2026-11-03","2026-08-11T15:04:12.928-0300","2026-08-11T15:04:12.955-0300"),
 ("EG0285-18","Tarefas pendentes","new","EG0285","2026-11-09",None,"2026-05-14T11:31:30.030-0300"),
 ("EG0285-14","Tarefas pendentes","new","EG0285","2026-11-09",None,"2026-05-14T11:31:11.610-0300"),
 ("EG0274-66","Tarefas pendentes","new","EG0274","2026-11-18",None,"2026-05-28T17:47:05.587-0300"),
 ("EG0274-65","Tarefas pendentes","new","EG0274","2026-11-18",None,"2026-05-28T17:47:08.171-0300"),
 ("EG0274-57","Tarefas pendentes","new","EG0274","2026-11-30",None,"2026-08-20T17:04:14.132-0300"),
 ("EG0241-45","Tarefas pendentes","new","EG0241","2026-11-30",None,"2026-09-21T14:45:40.371-0300"),
],
}

def stored(name):
    rows = json.load(open(os.path.join(D, name + '.json'), encoding='utf-8'))
    return [(i['key'], i['fields']['status']['name'],
             i['fields']['status']['statusCategory']['key'],
             i['fields']['project']['key'], i['fields'].get('duedate'),
             i['fields'].get('resolutiondate'), i['fields'].get('updated')) for i in rows]

bad = 0
for name, live in LIVE.items():
    got = stored(name)
    if got == live:
        print('OK    %-22s %d registros' % (name, len(live)))
    else:
        bad += 1
        print('DELTA %-22s ao vivo=%d gravado=%d' % (name, len(live), len(got)))
        for a, b in zip(live, got):
            if a != b: print('   live  ', a, '\n   snap  ', b)
        sl, sg = {r[0] for r in live}, {r[0] for r in got}
        if sl - sg: print('   so ao vivo:', sorted(sl - sg))
        if sg - sl: print('   so gravado:', sorted(sg - sl))
sys.exit(1 if bad else 0)
