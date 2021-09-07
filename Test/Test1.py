
N,k = 50,3
Cust = [[0,0,15],
        [10,10,11],
        [15,10,40]]

Time = max(Cust[:][0])
T_cust = []
res = 0
k=len(Cust)
flag = [0]*int(k)
for i in range(len(Cust)):
    T_cust.append(min(abs(Cust[i][2]-Cust[i][1]),int(N)-abs(Cust[i][2]-Cust[i][1])))    
T_cust = T_cust*5

for t in range(min(Cust[:][0]),Time+1):
    for i in range(int(k)):
        if Cust[i][0] <= t and flag[i] == 0:
            flag[i] = 1
        if t - Cust[i][0] >= T_cust[i] and flag[i] == 1:
            flag[i] = 0
    res = max(res,sum(flag))
print(res)  


