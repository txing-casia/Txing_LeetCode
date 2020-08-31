import math
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


class Solution(object):
    def maxCoins(self, piles):
        piles_sort=sorted(piles)
        return sum(piles_sort[int(len(piles)/3)::2])



def main():
    piles = [2,4,1,2,7,8]
    solution=Solution().maxCoins(piles)
    print(solution)


if __name__ == "__main__":
    main()

