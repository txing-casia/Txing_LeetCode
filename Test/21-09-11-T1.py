def minTurn(grid): 
    
    if not grid or not grid[0]:
        return 0
    r,c = len(grid),len(grid[0])
    dp = [[0]*c for _ in range(r)]
    oold_1,oold_2 = 0,0

    # for i in range(1,r):
    #     if grid[i][0] == 1:
    #         dp[i][0] = -1
    # for j in range(1,c):
    #     if grid[0][j] == 1:
    #         dp[0][j] = -1

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 0:
                # 寻找上上步的最少转弯数oold
                if dp[i][j-1] != -1 and grid[i][j-2] != 1 and grid[i-1][j-1] != 1:
                    oold_1 = min(dp[i][j-2],dp[i-1][j-1])
                elif dp[i][j-1] != 0 and grid[i][j-2] != 1 and grid[i-1][j-1] == 1:
                    oold_1 = dp[i][j-2]
                elif dp[i][j-1] != -1 and grid[i][j-2] == 1 and grid[i-1][j-1] != 1:
                    oold_1 = dp[i-1][j-1]
                if dp[i-1][j] != -1 and grid[i-1][j-1] != 1 and grid[i-2][j] != 1:
                    oold_2 = min(dp[i-1][j-1],dp[i-2][j])
                elif dp[i][j-1] != -1 and grid[i-1][j-1] != 1 and grid[i-2][j] == 1:
                    oold_2 = dp[i-1][j-1]
                elif dp[i][j-1] != -1 and grid[i-1][j-1] == 1 and grid[i-2][j] != 1:
                    oold_2 = dp[i][j-2]
                oold = min(oold1,oold2)
            
                if oold == dp[i-1][j-1]:
                	dp[i][j] = oold + 1
                else:
                    dp[i][j] = oold

            elif grid[i][j] == 1:
                dp[i][j] = -1
    return dp[-1][-1]

grid = [[0,0,0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0, 0],
[0, 0, 0, 0, 1, 0, 1],
[0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 0]]
print(minTurn(grid))