# 30%, 运行超时

# x,y,r = map(int,input().strip().split(' '))
N,T,C = 4,2,2
A = [1,2,3,1]

flag = 0
flag2 = -1
def search(it,Ct):
    if it+Ct>len(A):
        flag = 1
        return 0
    for j in range(it,it+Ct):
        if A[j] > T:
            flag2 = j
            return 0
    return 1
ans = 0
for i in range(N):
    if flag2 >= i:
        continue
    ans += search(i,C)
    if flag == 1:
        break

print(ans)






