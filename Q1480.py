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


###############################################################
class TreeNode(object):
    def __init__(self,data = 0,left = None,right = None):
        self.val = data
        self.left = left
        self.right = right

###############################################################
###############################################################
###############################################################

class Solution(object):
    def runningSum(self, nums):
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        return nums


def main():
    nums = [1,1,1,1,1]
    solution=Solution().runningSum(nums)
    print(solution)


if __name__ == "__main__":
    main()

