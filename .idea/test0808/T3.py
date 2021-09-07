# A = list(map(int,input().strip().split()))


A='()DD'
N=len(A)



def scort(temp):
    count=0
    for i in range(len(temp)):
        if temp[i] == '(':
            count += 1
        elif temp[i] == ')' :
            count -= 1
    return -count

space = 0
temp=''
S=[]
for i in range(N):
    if A[i] == '(' or A[i] == ')': 
        temp += A[i]
        space += 1
    if A[i] == 'L' and space != 0:
        space -= 1
    elif A[i] == 'L' and space == 0:
        space = space
    if A[i] == 'R' and space != N:
        space += 1
    elif A[i] == 'R' and space == N:
        space = space 
    if A[i] == 'D' and space != 0:
        temp = list(temp)
        temp.remove(temp[space-2])
        temp = str(''.join(temp))
    S.append(scort(temp))
print(S,end=' ')
    
