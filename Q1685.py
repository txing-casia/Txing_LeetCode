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
    def getSumAbsoluteDifferences(self, nums):
        N = len(nums)
        sum = 0
        output = []
        prefixSum =[]
        for i in range(N):
            sum += nums[i]
            prefixSum.append(sum) # 前i项和
        for i in range(N):
            output.append((i+1)*nums[i]-prefixSum[i] + prefixSum[N-1]-prefixSum[i]-nums[i]*(N-1-i))
        return output





def main():
    nums = [2,3,5]
    solution=Solution().getSumAbsoluteDifferences(nums)
    print(solution)


if __name__ == "__main__":
    main()

