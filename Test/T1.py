class Solution:
    def F(self, n):
        dp = [0]*n 
        dp[0] = 1
        dp[1] = 2
        if n > 2:
            for i in range(2,n):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n-1]
        elif n == 1:
            return dp[0]
        elif n == 2:
            return dp[1]
        

def main():
    n = 5
    Sol = Solution().F(n)
    print(Sol)

if __name__ == "__main__":
    main()



