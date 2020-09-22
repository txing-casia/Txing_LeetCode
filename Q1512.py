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
class TreeNode(object):
    def __init__(self,data = 0,left = None,right = None):
        self.val = data
        self.left = left
        self.right = right

###############################################################
###############################################################
###############################################################

class Solution(object):
    def numIdenticalPairs1(self, nums):
        if not nums:
            return
        n=len(nums)
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    ans+=1
        return ans


    def numIdenticalPairs2(self, nums: List[int]) -> int:
        m = collections.Counter(nums)
        return sum(v * (v - 1) // 2 for k, v in m.items())


def main():
    nums =[1,2,3,1,1,3]
    solution=Solution().numIdenticalPairs2(nums)
    print(solution)

if __name__ == "__main__":
    main()

