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
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


    def maxDepth2(self, root):
        if root is None:
            return 0
        queue = [(root, 1)]
        max_dep = 0
        while queue:
            node, depth = queue.pop()
            max_dep = max(max_dep, depth)
            if node.left:
                queue.append((node.left, depth +1))
            if node.right:
                queue.append((node.right, depth + 1))
        return max_dep



def main():
    root = ListNode([3])
    solution=Solution().maxDepth2(root)
    print(solution)


if __name__ == "__main__":
    main()

