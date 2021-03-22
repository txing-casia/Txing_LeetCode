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
    def hammingWeight(self, n: int) -> int:
        return sum(1 for i in range(32) if n & (1 << i)) 
    
    def hammingWeight1(self, n: int) -> int:
        ret = 0
        while n:
            n &= n - 1
            ret += 1
        return ret


def main():
    input = 11111111111111111111111111111101
    input= 1011
    solution=Solution().hammingWeight(input)
    print(solution)


if __name__ == "__main__":
    main()


