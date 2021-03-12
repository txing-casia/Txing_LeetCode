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
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)

    def maxSubArray1(self, nums) -> int:
        sumA = dp = nums[0]
        for i in range(1,len(nums)):
            dp = max(dp + nums[i], nums[i])
            sumA = max(sumA, dp)
        return sumA

def main():
    nums = [1, 1, 1, -5, 1, 1]
    solution=Solution().maxSubArray1(nums)
    print(solution)


if __name__ == "__main__":
    main()


