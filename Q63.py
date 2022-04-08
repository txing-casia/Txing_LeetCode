import math
from enum import Enum
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
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1
            else:
                break



        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


def main():
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    solution=Solution().uniquePathsWithObstacles(mat)
    print(solution)


if __name__ == "__main__":
    main()



    
