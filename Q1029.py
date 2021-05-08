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
    def twoCitySchedCost(self, costs) -> int:
        N=len(costs)
        deltacost=[]
        COSTAB=0
        for i in range(N):# 改派i去A城，花费变动deltacost[i]
            deltacost.append(costs[i][0]-costs[i][1])
            COSTAB=COSTAB+costs[i][1]
        deltacost=sorted(deltacost)
        for i in range(round(N/2)):
            COSTAB=COSTAB+deltacost[i]
        return COSTAB



def main():
    costs = [[10,20],[30,200],[400,50],[30,20]]
    solution=Solution().twoCitySchedCost(costs)
    print(solution)


if __name__ == "__main__":
    main()
