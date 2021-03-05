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
    def minIncrementForUnique(self, A) -> int:
        A.sort()
        res = 0
        i = 0
        while( i < len(A)-1 ):
            if A[i] >= A[i+1]:
                A[i+1] = A[i+1] + 1
                res += 1
            else:
                i += 1

        return res

    def minIncrementForUnique1(self, A) -> int:
        count = [0] * 80000
        # 建立一个 Hash 表，记录每个元素出现的次数
        for x in A:
            count[x] += 1
        # taken记录从冗余数中取走了几个
        ans = taken = 0
        for x in range(80000):
            if count[x] >= 2:
                taken += count[x] - 1
                ans -= x * (count[x] - 1)
            elif taken > 0 and count[x] == 0:
                taken -= 1
                ans += x
        
        return ans

    def minIncrementForUnique2(self, A) -> int:
        A.sort()
        A.append(100000)
        ans = taken = 0

        for i in range(1, len(A)):
            if A[i - 1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i] - A[i - 1] - 1)
                ans += give * (give + 1) // 2 + give * A[i - 1]
                taken -= give

        return ans




def main():
    A = [3,2,1,2,1,7]
    solution=Solution().minIncrementForUnique2(A)
    print(solution)


if __name__ == "__main__":
    main()


