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
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

    def divisorGame1(self, N: int) -> bool:
        f=[False]*(N+5)
        f[1]=False
        f[2]=True
        for i in range(3,N+1):
            for j in range(1,i):
                if i%j==0 and not(f[i-j]):
                    f[i]=True
                    break
        return f[N]
        





def main():
    N = 5
    solution=Solution().divisorGame1(N)
    print(solution)


if __name__ == "__main__":
    main()


