# N = 5
# nums = [1, 2, 2, 3, 4]



# def splitnums(N,nums):
#     Sum = sum(nums)
#     if N <= 1 or Sum % 2 !=0:
#         return str('No solution!')
#     tar = Sum // 2
#     dp = [False] * (tar+1)
#     dp[0] = True
#     ans = 0
#     for j in nums:
#         for i in range(tar,j-1,-1):
#             dp[i] = dp[i] or dp[i-j]
#             if dp[tar] == True:
#                 ans += 1
#                 dp[i] = False
#     # if dp[tar] == True:
#     #     res += 1
#     return ans

# print(splitnums(N,nums))


#############################

n, k = 3, 0
nums = [1, 2, 3]
nums_1 = nums
def largestsum(nums):
    if not nums:
        return 0
    def dfs(row):
        long = 0
        nums_1 = nums
        for dx in nums_1:
            newrow = dx
            nums_1.remove(dx)
            long += dx
            long = max(long, dfs(newrow) + long)
        return long 
    
    ans = 0
    nums = sorted(nums)
    for i in range(len(nums)):
        ans = max(ans,dfs(i))
    return ans

print(largestsum(nums))