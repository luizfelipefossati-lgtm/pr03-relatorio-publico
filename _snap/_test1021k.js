const fs=require('fs');
const h=fs.readFileSync('index.html','utf8');
const s=h.indexOf('<script>\n/* ====');const e=h.indexOf('</script>',s);
const code=h.slice(h.indexOf('>',s)+1,e);
global.window=global; global.console=console;
new Function(code)();
const T='issuetype in (Epic,"Fluxo de trabalho") ';
const q=[
 ['projetos','getVisibleJiraProjects',null],
 ['planned_2026-10',null,T+'AND duedate>="2026-10-01" AND duedate<="2026-10-31" ORDER BY duedate ASC'],
 ['overdue_2026-10',null,T+'AND duedate<"2026-10-01" AND statusCategory!=Done ORDER BY duedate ASC'],
 ['lookahead_2026-10',null,T+'AND duedate>="2026-11-01" AND duedate<="2026-12-31" ORDER BY duedate ASC'],
 ['sent_2026-10',null,T+'AND status changed to "Enviado - Aguardando Análise" DURING ("2026-10-01","2026-10-31")'],
 ['rework_2026-10',null,T+'AND status changed to "Enviado - Aguardando Análise" DURING ("2026-10-01","2026-10-31") AND status changed from "Enviado - Aguardando Análise"'],
 ['resolved_2026-10',null,T+'AND statusCategory=Done AND resolved>="2026-10-01" AND resolved<="2026-10-31"'],
 ['planned_2026-05',null,T+'AND duedate>="2026-05-01" AND duedate<="2026-05-31"'],
 ['planned_2026-06',null,T+'AND duedate>="2026-06-01" AND duedate<="2026-06-30"'],
 ['planned_2026-07',null,T+'AND duedate>="2026-07-01" AND duedate<="2026-07-31"'],
 ['planned_2026-08',null,T+'AND duedate>="2026-08-01" AND duedate<="2026-08-31"'],
 ['planned_2026-09',null,T+'AND duedate>="2026-09-01" AND duedate<="2026-09-30"'],
];
(async()=>{
 for(const [label,tool,jql] of q){
  if(tool){const r=await window.cowork.callMcpTool('mcp__Atlassian__'+tool,{});
   console.log(label,'->',r.structuredContent.values.length,'projetos');}
  else{const r=await window.cowork.callMcpTool('mcp__Atlassian__searchJiraIssuesUsingJql',{jql});
   console.log(label,'->',r.structuredContent.issues.nodes.length);}
 }
 console.log('__HISTORY__ meses:',Object.keys(window.__HISTORY__).sort().join(','));
})();
