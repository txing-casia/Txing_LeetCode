import sys
n = 5
K = 2
recode = [[1, 1, 1],
[2, 1, 1],
[3, 1, 1],
[5, 1, 1],
[4, 1, 2]]
hash_people={}
people=[[0]*5 for i in range(n)]
i=0

for line in recode:
    if line[0] in hash_people and line[1] == 1:
        continue
    else:
        hash_people[line[0]] = 1
    
    if i!=0:
        people[i][:] = people[i-1][:]

    if line[1] == 1 and people[i][line[2]-1] < K:
        people[i][line[2]-1] += 1
    elif line[1] == 0:
        people[i][line[2]-1] -= 1
    i+=1
res = list(people)
# print(str(people[1][:]).replace('[','').replace(']','').replace(',',' '))


for i in range(n):
    for j in range(5):
        a = str(people[i][j]).replace('[','').replace(']','').replace(',',' ')
        if j == 4: 
            print(int(a),end='\n')
        else:
            print(int(a),end=' ')

