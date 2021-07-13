import math
import collections
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
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        n, m = len(board), len(board[0])

        def dfs(x, y):
            # 如果board[x][y]不是位于矩阵边框，且字符为'x'，则返回为空
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return
            # 对于位于矩阵边框，且字符为'0'的元素
            board[x][y] = "A"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        # 检测边框
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        # 检测边框
        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

#################################

    def solve_BFS(self, board ) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        n, m = len(board), len(board[0])
        # 边框有'0'就放入队列
        que = collections.deque()
        for i in range(n):
            if board[i][0] == "O":
                que.append((i, 0))
            if board[i][m - 1] == "O":
                que.append((i, m - 1))
        for i in range(m - 1):
            if board[0][i] == "O":
                que.append((0, i))
            if board[n - 1][i] == "O":
                que.append((n - 1, i))
        # 队列中的每个元素标记为'A'
        while que:
            x, y = que.popleft()
            board[x][y] = "A"
        # 检测周围的4个点是否为非边框，且值为'0'，如果是，则加入队列
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < n and 0 <= my < m and board[mx][my] == "O":
                    que.append((mx, my))
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

def main():
    # [["X"]] 
    # [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    solution=Solution().solve_BFS(board)
    print(board)


if __name__ == "__main__":
    main()
