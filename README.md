# PR.03 - Relatorio de Indicadores de EPICs

Snapshot estatico publico do dashboard **Estudos e Projetos - Relatorio de Indicadores** (Engeplus Engenharia).

- **Ultima atualizacao:** 22/08/2026 18:12 (2026-08-22T18:12:38-03:00)
- **Fonte:** Jira Cloud - projetos-engeplus.atlassian.net
- **Escopo:** issues de nivel Epic (`Epic` e `Fluxo de trabalho`) dos projetos visiveis no site
- **Natureza dos dados:** congelados no momento da geracao. A pagina **nao** consulta o Jira ao vivo.

## Abas

| Aba | Periodo | Origem dos dados |
| --- | --- | --- |
| Julho 2026 | 01/07 a 31/07/2026 | congelado neste snapshot |
| Agosto 2026 | 01/08 a 31/08/2026 | congelado neste snapshot |
| Visao Acumulada | ultimos 6 meses (Mar a Ago/2026) | historico embutido + snapshot |

## Indicadores

- **OTD (On Time Delivery)** - percentual de epics previstos no mes que foram entregues.
- **Pendentes do mes** - previstos e nao entregues dentro do proprio mes.
- **Em atraso (acumulado)** - epics de meses anteriores com `duedate` vencido e status diferente de concluido.
- **Retrabalho** - epics que sairam do status "Enviado - Aguardando Analise" apos terem entrado nele.

## Publicacao

O commit e o push para o GitHub sao feitos automaticamente pela tarefa
`PR03-Auto-Push-GitHub` do Windows Task Scheduler (a cada 30 minutos).
O deploy no Vercel ocorre cerca de 1 minuto depois do push.

## Observacoes

- Existem variantes ortograficas do status de envio no Jira ("Enviado - Aguardando Analise",
  "Enviado- Aguardando Analise", "Enviado - Aguardando Analise1"). As metricas de envio e
  retrabalho usam a grafia padrao, portanto podem subestimar o total em projetos que adotaram
  as variantes.
- O projeto EG0280 - DMAE tem chave `G0280` no Jira.
- Os dados publicados contem chaves e titulos de epics, nomes de projetos e nomes de status.
  Nao contem e-mails, identificadores de conta nem avatares.
