import collections
# 模拟ACM数据格式 

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# grid = [[0,0,0,0,1,0,0,0,0,0,0,0,0]]

# def DFS(i,j):
#     if 0<=i and i<r and 0<=j and j<c and grid[i][j] == 1:
#         grid[i][j] = 0
#         return 1 + DFS(i-1,j) + DFS(i+1,j) + DFS(i,j-1) + DFS(i,j+1)
#     else:
#         return 0

# r , c = len(grid),len(grid[0])
# fin_res = 0
# for i in range(r):
#     for j in range(c):
#         fin_res = max(DFS(i,j),fin_res)
# print(fin_res)

######################
# BFS
######################
r , c = len(grid) , len(grid[0])
total_res = 0
for i in range(r):
    for j in range(c):
        ans = 0
        que = []
        if grid[i][j] == 1:
            grid[i][j] = 0
            ans += 1
            que.append((i,j))
            while que:
                cur_r,cur_c = que.pop(0)
                for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    temp_r , temp_c = cur_r + dr , cur_c + dc
                    if 0<=temp_r and temp_r<r and 0<=temp_c and temp_c<c and grid[temp_r][temp_c] == 1:
                        grid[temp_r][temp_c] = 0
                        ans += 1
                        que.append((temp_r,temp_c))
        total_res = max(total_res,ans)
print(total_res)





######################
# BFS + 队列
######################
# ans = 0
# for i, l in enumerate(grid):
#     for j, n in enumerate(l):
#         cur = 0
#         q = collections.deque([(i, j)])
#         while q:
#             cur_i, cur_j = q.popleft()
#             if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
#                 continue
#             cur += 1
#             grid[cur_i][cur_j] = 0
#             for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
#                 next_i, next_j = cur_i + di, cur_j + dj
#                 q.append((next_i, next_j))
#         ans = max(ans, cur)
# print(ans)



