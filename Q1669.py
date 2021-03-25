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




class Solution:
    def mergeInBetween(self, list1, a: int, b: int, list2):
        res = list1 # 存放答案头指针，在list1基础上合并
        num = 0 # 计数器
        while list1:
            # 找到 list1 的 a 处指针放入 start1
            if num == a-1: 
                start1 = list1
            # 找到 list1 的 b 处指针放入 end1
            if num == b+1:
                end1 = list1
                break
            list1 = list1.next
            num += 1
        # 找到 list2 的 尾部指针放入 end2
        start1.next = list2
        while list2.next: 
            list2 = list2.next
        list2.next = end1
        return res


def main():
    list1 = stringToListNode([0,1,2,3,4,5])
    list2 = stringToListNode([1000000,1000001,1000002])
    a = 3
    b = 4
    solution=Solution().mergeInBetween(list1,a,b,list2)
    print(solution)


if __name__ == "__main__":
    main()


