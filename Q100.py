import math
from enum import Enum
import bisect
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

class TreeNode():
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.data)
        


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.data != q.data:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2


def main():
    p = TreeNode([1,2,1])
    q = TreeNode([1,1,2])

    solution=Solution().isSameTree(p,q)
    print(solution)


if __name__ == "__main__":
    main()


