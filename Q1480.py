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
class TreeNode(object):
    def __init__(self,data = 0,left = None,right = None):
        self.val = data
        self.left = left
        self.right = right

###############################################################
###############################################################
###############################################################

class Solution(object):
    def kidsWithCandies1(self, candies , extraCandies ) :
        sort_candies=sorted(candies)
        ans=list()
        for i in range(len(candies)):
            if candies[i]+extraCandies>=sort_candies[-1]:
                ans.append(bool(1))
            else:
                ans.append(bool(0))
        return ans

    def kidsWithCandies2(self, candies , extraCandies ) :
        maxCandies = max(candies)
        ret = [candy + extraCandies >= maxCandies for candy in candies]
        return ret

def main():
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    solution=Solution().kidsWithCandies1(candies,extraCandies)
    print(solution)


if __name__ == "__main__":
    main()

