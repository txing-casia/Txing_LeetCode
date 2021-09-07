N,M=4,1
L=[1,2,3,4]


ans = 0
nums = L
T=[]
# def search(T,i):
#     if i >= N-1:
#         return 0
#     if T[i] <= T[i+1]+M:
#         return 1 + DFS(i+1)


for i in range(N):
    T.append(nums.pop(nums(i)))
    ans += search(T,i) 

print(ans)

