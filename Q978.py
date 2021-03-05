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
    def maxTurbulenceSize(self, arr) -> int:
        n = len(arr)
        res = 1
        left,right=0,0

        while(right<n-1):
            if left == right:
                # 右边界元素等于右边界+1的元素
                if arr[right] == arr[right+1]:
                    left+=1
                right+=1
            else:
                # 在扩展长度时候，只考虑验证右边界条件即可
                if (arr[right - 1] < arr[right]) and (arr[right] > arr[right + 1]):
                    right+=1    
                elif (arr[right - 1] > arr[right]) and (arr[right] < arr[right + 1]):
                    right+=1
                else:
                # 右边界不符合条件则验证结束，将left右移，重新验证
                    left = right
            res = max(res, right - left + 1)

        return res


    def maxTurbulenceSize1(self, arr) -> int:
        n = len(arr)
        dp = [[0 for i in range(2)] for j in range(n)]
        dp[0][0] = dp[0][1] = 1
        for i in range(n):
            if arr[i-1] > arr[i]:
                dp[i][0] = dp[i-1][1] + 1
                dp[i][1] = 1
            elif arr[i-1] < arr[i]:
                dp[i][1] = dp[i-1][0] + 1
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i][1] = 1

        res = 1
        for i in range(n):
            res = max(res, dp[i][0])
            res = max(res, dp[i][1])

        return res


    def maxTurbulenceSize2(self, arr) -> int:
        n = len(arr)
        res = 1
        dp0 = dp1 = 1
        # 注意要从1开始循环
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                dp0 = dp1 + 1
                dp1 = 1
            elif arr[i-1] < arr[i]:
                dp1 = dp0 + 1
                dp0 = 1
            else:
                dp0 = dp1 = 1

            res = max(res, dp0)
            res = max(res, dp1)

        return res


def main():
    inputs = [4,8,12,16]# [0,1,1,0,1,0,1,1,0,0] # [9,4,2,10,7,8,8,1,9]
    solution=Solution().maxTurbulenceSize2(inputs)
    print(solution)


if __name__ == "__main__":
    main()


