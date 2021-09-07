import math
from enum import Enum
import bisect
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    

def stringToListNode(input):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in input:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]" # 最后一个逗号不输出




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


def main():
    mat=[[1,2,3],[4,5,6],[7,8,9]]
    solution=Solution().solve(mat)
    print(solution)


if __name__ == "__main__":
    main()


