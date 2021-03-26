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
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1, node2 = temp.next, temp.next.next
            temp.next = node2
            # 下面两行的顺序不能交换，否则出现循环
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next

    def swapPairs1(self, head: ListNode) -> ListNode:
        # 链表为空，结束迭代
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead


def main():
    head = stringToListNode([1,2,3,4,5])
    solution=Solution().swapPairs1(head)
    print(solution)


if __name__ == "__main__":
    main()


