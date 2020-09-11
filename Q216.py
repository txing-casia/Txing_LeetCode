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
###############################################################
###############################################################

class Solution(object):
    def combinationSum3(self, k: int, n: int):
        def dfs(temp,S,k,n):
            if len(temp)==k and n==0:
                ans.append(temp[:])
                return
            for i in range(len(S)):
                temp.append(S[i])
                # S[i + 1:]实现了剪枝和防止逆序选数，这是关键点
                dfs(temp, S[i+1:], k, n-S[i])
                temp.pop()
        ans=[]
        S=[i for i in range(1,10)]
        # 暂存数组，可选项，需要k个数，需要和为n
        dfs([], S, k, n)
        return ans





        # def backtrack(nums, tmp, n, k):
        #     if len(tmp) == k and n == 0:
        #         res.append(tmp[:])
        #         return
        #     for i in range(len(nums)):
        #         tmp.append(nums[i])
        #         backtrack(nums[i + 1:], tmp, n - nums[i], k)    # nums[i + 1:]实现了剪枝和防止逆序选数，这是关键点
        #         tmp.pop()
        # res = []
        # nums = [i for i in range(1, 10)]
        # backtrack(nums, [], n, k)
        # return res





def main():
    k = 3
    n = 9
    solution=Solution().combinationSum3(k,n)
    print(solution)


if __name__ == "__main__":
    main()

