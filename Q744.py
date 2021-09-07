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
    def nextGreatestLetter(self, letters, target: str) -> str:
        for i in range(1,26):
            ans = chr((ord(target) - ord('a') + i ) % 26 + ord('a'))
            if ans in letters:
                return ans
        return None

    def nextGreatestLetter2(self, letters, target: str) -> str:
        L = 0
        R = len(letters) - 1
        while L <= R:
            M = L + (R - L) // 2
            if letters[M] <= target:
                L = M + 1
            elif letters[M] > target:
                R = M - 1
        return letters[L % len(letters)]




def main():
    letters = ["c", "f", "j"]
    target = "j"
    solution=Solution().nextGreatestLetter2(letters, target)
    print(solution)


if __name__ == "__main__":
    main()


