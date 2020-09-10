import math
import collections
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

###############################################################
###############################################################
###############################################################

class Solution(object):
    def combinationSum2(self, candidates, target):
        def dfs(pos: int, rest: int):
            # nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量
            # sequence 用来暂存序列
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:]) # 添加答案
                return
            if pos == len(freq) or rest < freq[pos][0]: # sequence不行，停止
                return

            dfs(pos + 1, rest)

            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]

        # 为数据出现次数计数[(数据1，出现次数),(数据2，出现次数)]
        freq = sorted(collections.Counter(candidates).items())
        ans = list()
        sequence = list()
        # inputs: 序号，剩余的target
        dfs(0, target)
        return ans

def main():
    candidates = [10,1,2,7,6,1,5]
    target = 8
    solution=Solution().combinationSum2(candidates,target)
    print(solution)


if __name__ == "__main__":
    main()

