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

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def __str__(self):
    #     self.data=str(self.data)

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return 
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[: mid])
        root.right = self.sortedArrayToBST(nums[mid + 1: ])
        return root 





def main():
    nums = [7,1,5,3,6,4]
    solution=Solution().sortedArrayToBST(nums)
    print(solution)


if __name__ == "__main__":
    main()



    
    

