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
    def combinationSum1(self, candidates, target):
        ans = []
        temp = []
        def recursion(idx, res):
            if idx >= len(candidates) or res >= target:
                if res == target:
                    ans.append(temp[:])
                return
            temp.append(candidates[idx])
            recursion(idx, res + candidates[idx])
            temp.pop()
            recursion(idx + 1, res)
        recursion(0, 0)
        return ans


    def combinationSum2(self, candidates, target):
        ans=[] # 汇总可行解
        temp=[] # 存放当前解
        def recursion(idx,sum):
            if idx >= len(candidates) or sum >= target: # 判断合法
                if sum - target == 0:
                    ans.append(temp[:])
                return
            temp.append(candidates[idx])
            recursion(idx, sum + candidates[idx])
            temp.pop()
            recursion(idx + 1, sum)
        recursion(0,0)
        return ans

def main():
    candidates = [2, 3, 6, 7]
    target = 7
    solution=Solution().combinationSum2(candidates,target)
    print(solution)


if __name__ == "__main__":
    main()

