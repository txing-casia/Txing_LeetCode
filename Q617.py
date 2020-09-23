import math
import collections
from enum import Enum
from typing import List

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


###############################################################
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

###############################################################
###############################################################
###############################################################

class Solution(object):
    class Solution:
        def mergeTrees(self, t1 , t2 )  :
            if not t1:
                return t2
            if not t2:
                return t1

            merged = TreeNode(t1.val + t2.val)
            merged.left = self.mergeTrees(t1.left, t2.left)
            merged.right = self.mergeTrees(t1.right, t2.right)
            return merged



def main():
    t1=TreeNode([1, 3, 2, 5])
    t2=TreeNode([2, 1, 3, None, 4, None, 7])
    solution=Solution().mergeTrees(t1,t2)
    print(solution)


if __name__ == "__main__":
    main()

