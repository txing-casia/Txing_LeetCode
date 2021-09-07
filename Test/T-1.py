# AC

import sys
L='a:13,b:5,c:2@' 
L1,L2=L.split('@')
L1_hash={}
L2_hash={}
for ex in L1.split(','):
    L1_hash[ex[0]]=int(ex[2:])
if L2 != '':
    for ex in L2.split(','):
        if ex[0] in L1_hash:
            L1_hash[ex[0]]=L1_hash[ex[0]]-int(ex[2:])

res=[]
for ex in L1.split(','):
    if L1_hash[ex[0]] != 0:
        res=str(res)+','+str(ex[0])+':'+str(L1_hash[ex[0]])

    
print(res[3:])



