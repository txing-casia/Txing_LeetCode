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
    def generateParenthesis(self, n: int):
        def generate(A):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: # 合法字符串只可能出现差右括号的情况，不会差左括号 
                    return False
            return bal == 0

        ans = []
        generate([])
        return ans

  ##############################

    def generateParenthesis2(self, n: int):
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans  

  ##############################

    def generateParenthesis3(self, n: int):
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis3(c):
                for right in self.generateParenthesis3(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans



def main():
    n = 3
    solution=Solution().generateParenthesis3(n)
    print(solution)


if __name__ == "__main__":
    main()


