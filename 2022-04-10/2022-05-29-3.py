

try:
    # n = int(input())
    # nums = list(map(int,input().strip().split()))
    n = 5
    nums = [5,1,3,2,4]   
    # nums = sorted(nums) 
    dp = [0]*n
    
    for i in range(1,n):
        if sum(nums)//nums[0] >= sum(nums)//nums[-1]:
            dp[i] = dp[i-1] + sum(nums)//nums[0]
            nums.pop(0) #start
        else:
            dp[i] = dp[i-1] + sum(nums)//nums[-1]
            nums.pop() # end
        
    print(dp[-1]+1)


except:
    pass