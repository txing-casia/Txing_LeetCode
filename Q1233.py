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
    def removeSubfolders(self, folder):
        # 首先对folder排序，然后把第一个文件夹放入res中。但我们可以理解为，最短的文件夹一定不是一个子文件夹，否则还会有一个更短的父文件夹。然后遍历folder，因为已经排序了，所以每次只和res最后一个比较就可以。如果开头部分不相同，说明当前遍历到了一个新的文件夹目录，加入res。
        folder.sort()
        # 这里看似取巧，但我们可以理解为，最短的文件夹一定不是一个子文件夹，否则还会有一个更短的父文件夹。
        roots = [folder[0]]
        for i in range(1, len(folder)):
            fd = folder[i]
            if not fd.startswith(roots[-1] + "/"):
                roots.append(fd)
        return roots



def main():
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    solution=Solution().removeSubfolders(folder)
    print(solution)


if __name__ == "__main__":
    main()


