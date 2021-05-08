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
    def wiggleMaxLength(self, nums) -> int:
        N = len(nums)
        if N == 1 or (N == 2 and nums[0] == nums[1]):
            return 1
        ans = 1
        for i in range(1,N-1):
            dif_old = nums[i] - nums[i-1]
            length = 2
            for j in range(i+1,N):
                dif_new = nums[j] - nums[j-1]
                if dif_old * dif_new < 0:
                    length += 1
                    ans = max(length,ans) 
                    dif_old = dif_new
                elif dif_new != 0:
                    ans = max(length,ans) 
                    dif_old = dif_new
        return ans

    def wiggleMaxLength1(self, nums) -> int:
        N = len(nums)
        if N == 1 or (N == 2 and nums[0] == nums[1]):
            return 1
        ans = 1
       
        dif_old = nums[1] - nums[0]
        length = 2
        for j in range(1,N):
            dif_new = nums[j] - nums[j-1]
            if dif_old * dif_new < 0:
                length += 1
                ans = max(length,ans) 
                dif_old = dif_new
            elif dif_new != 0:
                ans = max(length,ans) 
                dif_old = dif_new
        return ans

def main():
    nums = [1,17,5,10,13,15,10,5,16,8]
    solution=Solution().wiggleMaxLength1(nums)
    print(solution)


if __name__ == "__main__":
    main()

