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


class NumArray:

    def __init__(self, nums):
        self.sums = [0]
        _sums = self.sums
        for num in nums:
            _sums.append(_sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        _sums = self.sums
        return _sums[j + 1] - _sums[i]





def main():
    s = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    NumArray().__init__(s)
    solution=NumArray().sumRange(s)
    print(solution)


if __name__ == "__main__":
    main()

