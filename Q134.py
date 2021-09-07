# 
from typing import cast


gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

# gas = [3,1,1]
# cost = [1,2,2]

ans = -1
for step in range(len(gas)):
    start = step
    num_step = 0
    oil = gas[start]
    for i in range(step,len(gas)-1):
        oil -= cost[i] 
        if oil < 0:
            break
        oil += gas[i+1]
        num_step += 1

    oil -= cost[-1]
    if oil >= 0:
        oil += gas[0]
        num_step += 1
        if num_step == len(gas):
            ans = start
            break
    else:
        continue
    for j in range(step):
        oil -= cost[j]
        if oil < 0:
            break
        oil += gas[j+1]
        num_step += 1
        if num_step == len(gas):
            ans=start

print(ans)