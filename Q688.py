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



class Solution(object):
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K): # 走k步还在棋盘内的概率
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        # 走了一步之后还在棋盘内
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2
        # map()函数把sum依次作用在dp的每一项上，在map()外再使用sum()完成二维数组的求和
        return sum(map(sum, dp))

######################################

    def knightProbability2(self, N, K, sr, sc):
        def canonical(r, c):
            if 2 * r > N: r = N - 1 - r
            if 2 * c > N: c = N - 1 - c
            if r > c: r, c = c, r
            return r*N + c

        def matrix_mult(A, B):
            ZB = zip(*B)
            return [[sum(a * b for a, b in zip(row, col))
                    for col in ZB] for row in A]

        def matrix_expo(A, K):
            if K == 0:
                return [[+(i==j) for j in xrange(len(A))]
                        for i in xrange(len(A))]
            if K == 1:
                return A
            elif K % 2:
                return matrix_mult(matrix_expo(A, K-1), A)
            B = matrix_expo(A, K/2)
            return matrix_mult(B, B)

        index = [0] * (N*N)
        t = 0
        for r in xrange(N):
            for c in xrange(N):
                if r*N + c == canonical(r, c):
                    index[r*N + c] = t
                    t += 1
                else:
                    index[r*N + c] = index[canonical(r, c)]

        T = []
        for r in xrange(N):
            for c in xrange(N):
                if r*N + c == canonical(r, c):
                    row = [0] * t
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                    (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r+dr < N and 0 <= c+dc < N:
                            row[index[(r+dr)*N + c+dc]] += 0.125
                    T.append(row)

        Tk = matrix_expo(T, K)
        i = index[sr * N + sc]
        return sum(Tk[i])




def main():
    N, K, r, c = 3, 2, 0, 0
    solution=Solution().knightProbability(N, K, r, c)
    print(solution)


if __name__ == "__main__":
    main()

