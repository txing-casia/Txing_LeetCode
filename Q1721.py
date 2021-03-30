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
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        L=head
        num=0
        while L:
            num+=1
            if num == k-1: # 找到前k-1个结点
                FK=L
            L=L.next
        k=num-k
        num=0
        ans=L=head
        while L:
            num+=1
            if num == k:
                LK=L
                break
            L=L.next 

        FK2=FK.next
        FK3=FK.next.next
        LK2=LK.next
        LK3=LK.next.next
        
        FK.next=LK2
        LK2.next=FK3
        LK.next=FK2
        FK2.next=LK3

        return listNodeToString(ans)

    def swapNodes1(self, head: ListNode, k: int) -> ListNode:
        fast = head
        while k - 1 != 0: # 1 2 3 4 5 6 7  k=3 往后移2步到3
            fast = fast.next
            k -= 1
        L = fast # L = 3
        slow = head
        while fast.next: # slow = 5, fast = 7
            fast = fast.next
            slow = slow.next
        R = slow # R = 5
        
        L.val,R.val = R.val,L.val #3 和 5 的val 交换
        return head




def main():
    # head = stringToListNode([7,9,6,6,7,8,3,0,9,5])
    head = stringToListNode([1,2,3,4,5])
    k=3
    solution=Solution().swapNodes1(head,k)
    print(solution)


if __name__ == "__main__":
    main()


