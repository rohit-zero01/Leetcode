class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[[-1 for _ in range(3)]for _ in range(2)]for _ in range(n)]

        def f(i,buy,cap):
            if cap ==0 or i ==n:
                return 0

            profit = 0

            if dp[i][buy][cap] != -1:
                return dp[i][buy][cap]

            if buy==1:
                dp[i][buy][cap] = max(-prices[i] + f(i+1,0,cap), f(i+1,1,cap))
            else:
                dp[i][buy][cap] = max(prices[i] + f(i+1, 1, cap-1), f(i+1,0,cap))

            return dp[i][buy][cap] 

        return f(0,1,2)

            
        