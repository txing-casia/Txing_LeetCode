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
        n=len(nums)
        dp = nums
        for i in range(1,n):
            dp[i] = max( nums[i], dp[i-1] + nums[i])
        return max(dp)

    def maxSubArray1(self, nums) -> int:
        dp = 0
        maxA = nums[0]
        for i in range(len(nums)):
            dp = max( nums[i], dp + nums[i])
            maxA = max( dp, maxA )
        return maxA





def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution=Solution().maxSubArray1(nums)
    print(solution)


if __name__ == "__main__":
    main()


