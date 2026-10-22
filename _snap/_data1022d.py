# -*- coding: utf-8 -*-
"""Rodada 2026-10-22 18:33 UTC / 15:33 BRT (execucao agendada, autonoma).

Todas as 7 chamadas dinamicas do artifact foram refeitas ao vivo contra o Jira
(cloud ead785de-33f3-4746-9bdb-a2a58cf5213b) pelo conector MCP Atlassian:
getVisibleJiraProjects + as 6 consultas JQL do mes corrente (out/2026).

planned=15 overdue=0 lookahead=33 sent=6 resolved=6 rework=4 | projects=21

Conferencia contra os JSONs ja gravados em _snap/ (rodada _data1022b, 16:01 UTC):
todos os 6 conjuntos e a lista de projetos IDENTICOS. O conjunto `resolved`
voltou com as mesmas 6 epics em outra ordem (a JQL do artifact nao tem ORDER BY,
entao a ordem de retorno do Jira nao e estavel); como o conteudo nao mudou, o
arquivo nao foi reescrito.

Nenhum JSON precisou ser reescrito; apenas index.html e snapshot-data.js foram
regerados com carimbo novo (2026-10-22T15:33:57-03:00).

Observacao operacional: a resposta de getVisibleJiraProjects estourou o limite
de tokens da ferramenta e foi processada a partir do arquivo salvo pelo proprio
conector, com extracao dos campos minimos (key, name, issueTypes[name,
hierarchyLevel]). Resultado conferido por MD5 canonico contra _projects_min.json:
c5873d9e86471ebc97cc091448095b42 em ambos os lados.
"""
