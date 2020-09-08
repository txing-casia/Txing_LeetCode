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

###############################################################
###############################################################
###############################################################

class Solution(object):
    def combine(self, n, k):
        if k > n or k == 0:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if k == n:
            return [[i for i in range(1, n + 1)]]

        answer = self.combine(n - 1, k)
        for item in self.combine(n - 1, k - 1):
            item.append(n)# select from [1.n-1],then append n
            answer.append(item)

        return answer



def main():
    n = 4
    k = 3
    solution=Solution().combine(n,k)
    print(solution)


if __name__ == "__main__":
    main()

