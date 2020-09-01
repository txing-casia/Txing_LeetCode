import math
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


class Solution(object):
    def PredictTheWinner_solution_1(self, nums):
        def total(start: int, end: int, turn: int) -> int:
            if start == end:
                return nums[start] * turn
            scoreStart = nums[start] * turn + total(start + 1, end, -turn) # case 1
            scoreEnd = nums[end] * turn + total(start, end - 1, -turn)# case 2
            return max(scoreStart * turn, scoreEnd * turn) * turn
        return total(0, len(nums) - 1, 1) >= 0

    def PredictTheWinner_solution_2(self, nums):
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for i, num in enumerate(nums):
            dp[i][i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][length - 1] >= 0

    def PredictTheWinner_solution_2_1(self, nums):
        length = len(nums)
        dp = [0] * length
        for i, num in enumerate(nums):
            dp[i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[length - 1] >= 0


def main():
    nums = [2,4,1,2,7,8]
    solution=Solution().PredictTheWinner_solution_2_1(nums)
    print(solution)


if __name__ == "__main__":
    main()

