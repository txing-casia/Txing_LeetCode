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
    def restoreString(self, s: str, indices ) -> str:
        result = [""] * len(s)
        for i, ch in enumerate(s):
            result[indices[i]] = ch
        return "".join(result)

    def restoreString1(self, s: str, indices ) -> str:
        # s=list(s)
        res=['']*len(s)
        for i in range(len(indices)):
            res[indices[i]]=s[i]
        return "".join(res)

    def restoreString2(self, s: str, indices ) -> str:
        s=list(s)
        for i in range(len(indices)):
            ch = s[i]
            idx = indices[i]
            while(idx!=i):
                ch,s[idx] = s[idx],ch
                idx,indices[idx] = indices[idx],idx
            s[i]=ch
            indices[i]=i
        return "".join(s)


def main():
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    solution=Solution().restoreString2(s,indices)
    print(solution)


if __name__ == "__main__":
    main()


