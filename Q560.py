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
    def subarraySum(self, nums, k):
        count=0
        for start in range(len(nums)):
            sum=0
            for end in range(start,-1,-1):
                sum+=nums[end]
                if sum == k:
                    count+=1
        return count

    def subarraySum1(self, nums, k):
        mp = {0: 1}
        count = 0
        pre = 0
        for x in nums:
            pre+=x
            if (pre - k) in mp:
                count += mp[pre - k]
            if pre in mp:
                mp[pre] += 1
            else:
                mp[pre] = 1
        return count
#     int subarraySum(vector<int>& nums, int k) {
#         unordered_map<int, int> mp;
#         mp[0] = 1;
#         int count = 0, pre = 0;
#         for (auto& x:nums) {
#             pre += x;
#             if (mp.find(pre - k) != mp.end()) {
#                 count += mp[pre - k];
#             }
#             mp[pre]++;
#         }
#         return count;
#     }







def main():
    nums = [1,1,1]
    target = 2
    solution=Solution().subarraySum1(nums,target)
    print(solution)


if __name__ == "__main__":
    main()


