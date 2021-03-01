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
    def findRepeatNumber(self, nums) -> int:
        Hash=dict()
        for i in range(len(nums)):
            if nums[i] not in Hash:
                Hash[nums[i]]=i
            else:
                return nums[i]
        return -1


def main():
    s = [35,1,2,3]
    solution=Solution().findRepeatNumber(s)
    print(solution)


if __name__ == "__main__":
    main()

