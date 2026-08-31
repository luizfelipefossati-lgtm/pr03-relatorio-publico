# -*- coding: utf-8 -*-
import json,os,sys
D=os.path.dirname(os.path.abspath(__file__))
PN={p['key']:p['name'] for p in json.load(open(os.path.join(D,os.pardir,'_projects_min.json'),encoding='utf-8'))}
def write(name,rows):
    out=[]
    for k,sm,st,cat,pj,du,rd,up in rows:
        out.append({"key":k,"fields":{"summary":sm,"status":{"name":st,"statusCategory":{"key":cat}},
                    "project":{"key":pj,"name":PN.get(pj,pj)},"duedate":du,"resolutiondate":rd,"updated":up}})
    json.dump(out,open(os.path.join(D,name+'.json'),'w',encoding='utf-8'),ensure_ascii=False)
    print('%-22s %d'%(name,len(out)))
