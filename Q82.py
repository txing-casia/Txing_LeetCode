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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 判断链表非空
        if not head:
            return head
        # 头节点可能要修改，需要添加虚头节点
        dummy = ListNode([])
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


    def deleteDuplicates1(self, head):
        if not head or not head.next:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            move = head.next
            while move and head.val == move.val:
                move = move.next
            return self.deleteDuplicates(move)
        return head


def main():
    head = stringToListNode([1,2,3,3,3,4,4,5])
    solution=Solution().deleteDuplicates(head)
    print(solution)


if __name__ == "__main__":
    main()
