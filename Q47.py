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
    def permuteUnique(self, nums):
        # 错误输入检测
        if not nums:
            return []

        def dfs(nums, temp_list):
            if len(temp_list) == n:
                ans.append(temp_list) # temp_list存满了就放入ans
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]: # 第一个元素不进行此判断
                    continue
                dfs(nums[:i]+nums[i+1:], temp_list+[nums[i]])

        ans = []
        n = len(nums)
        nums.sort()
        dfs(nums, [])
        return ans


def main():
    nums =[1,1,2]
    solution=Solution().permuteUnique(nums)
    print(solution)


if __name__ == "__main__":
    main()

