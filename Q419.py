
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

def DFS(cur_i,cur_j):
    if 0<=cur_i and cur_i<r and 0<=cur_j and cur_j<c and board[cur_i][cur_j] == 'X':
        board[cur_i][cur_j] = "."
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            DFS(cur_i+di,cur_j+dj)
    

r,c = len(board),len(board[0])
ans=0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'X':
            ans+=1
            DFS(i,j)

print(ans) 