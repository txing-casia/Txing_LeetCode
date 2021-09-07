class Solution:
    def solve(self , matrix):
        if not matrix:
            return 0
        def DFS(rr,cc): # 这个变量名不能和外部函数的变量名一样，否则matrix[n_r][n_c] > matrix[rr][cc]这里会出错
            res = 1
            for x , y in [(-1,0),(1,0),(0,1),(0,-1)]: # 上下左右
                n_r , n_c = rr + x, cc + y
                if 0 <= n_r < r and 0 <= n_c < c and matrix[n_r][n_c] > matrix[rr][cc]:
                    res = max(res , DFS(n_r , n_c) + 1)
            return res

        ans = 0
        r , c = len(matrix) , len(matrix[0])
        for i in range(r):
            for j in range(c):
                ans = max(ans, DFS(i,j))
        return ans




mat=[[1,2,3],[4,5,6],[7,8,9]]
sol=Solution().solve(mat)
print(sol)


# ''' 
# class Solution:
#     def clockwisePrint(self, mat, n, m):
#         res = []
#         while mat:
#             res += mat.pop(0)
#             if mat:
#                 mat = self.rotate(mat)
#         return res
        
#     def rotate(self,mat):
#         nn,mm = len(mat),len(mat[0])
#         nmat = []
#         for i in range(mm):
#             n_L = []
#             for j in range(nn):
#                 n_L.append(mat[j][mm-1-i])
#             nmat.append(n_L)
#         return nmat
# mat=[[1,2,3],[4,5,6],[7,8,9]]
# n,m=3,3
# sol=Solution().clockwisePrint(mat,n,m)
# print(sol)

# '''