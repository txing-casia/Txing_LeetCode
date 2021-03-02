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
    def balancedStringSplit(self, s: str) -> int:
        res,L,R=0,0,0
        for i in range(len(s)):
            if s[i] =='L':
                L+=1
            elif s[i]=='R':
                R+=1
            if L==R and L!=0:
                res+=1
                # 如果s中不限定只包含字符LR，则需置零L和R
        return res



def main():
    s = "RLRRLLRLRL"
    solution=Solution().balancedStringSplit(s)
    print(solution)


if __name__ == "__main__":
    main()

