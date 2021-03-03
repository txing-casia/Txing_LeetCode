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
    def minOperations(self, boxes: str):
        stepnum = len(boxes)
        # 浅拷贝创建二维数组，在赋值的时候，内存都指向同一位置，在赋值时会有问题
        # steps = [[0]*stepnum]*stepnum 
        # 创建二维数组的正确方式
        steps = [[0 for i in range(stepnum)] for j in range(stepnum)]
        ans=[]
        for i in range(stepnum): 
            for j in range(stepnum):
                if boxes[j] == '1':
                    steps[i][j] = abs(j-i)

        for i in range(stepnum):
            ans.append( sum(steps[i][:]) ) 
        return ans


    def minOperations1(self, boxes: str)  :
        dp = [0] * len(boxes)
        right = 0
        for i in range(len(boxes)): 
            if boxes[i] == '1':
                dp[0] += i
                right += 1   # 当前及其右边的 1 的数量
        
        left = 0
        for j in range(1, len(boxes)):
            if boxes[j-1] == '1':
                left += 1
                right -= 1
            dp[j] = dp[j-1] - right + left
            
        return dp




def main():
    s = "codeleet"
    boxes = "110"
    solution=Solution().minOperations1(boxes)
    print(solution)


if __name__ == "__main__":
    main()


