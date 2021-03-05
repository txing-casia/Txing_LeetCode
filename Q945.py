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
    def minIncrementForUnique(self, A ) -> int:
        Hash=dict()
        res=0
        for i in range(len(A)):
            Hash[A[i]] = i
        for i in range(len(A)):
            while(A[i] in Hash):
                A[i] += 1
                res += 1
                Hash[A[i]] = 1
                Hash[A[i]] = 2

        return res


def main():
    A = [3,2,1,2,1,7]
    solution=Solution().minIncrementForUnique(A)
    print(solution)


if __name__ == "__main__":
    main()


