# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         n = len(prices)
#         dp = [[[0 for _ in range(3)]for _ in range(2)]for _ in range(n+1)]

#         for i in range(n-1,-1,-1):
#             for buy in range(2):
#                 for cap in range(1,3):
#                     if buy==1:
#                         dp[i][buy][cap] = max(-prices[i] + dp[i+1][0][cap], dp[i+1][1][cap])
#                     else:
#                         dp[i][buy][cap] = max(prices[i] + dp[i+1][1][cap-1], dp[i+1][0][cap])

#         return dp[0][1][2]

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        
        # after represents dp[i+1], initialized to 0
        after = [[0 for _ in range(3)] for _ in range(2)]
        # current represents dp[i]
        current = [[0 for _ in range(3)] for _ in range(2)]
        
        for i in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy == 1:
                        current[buy][cap] = max(-prices[i] + after[0][cap], after[1][cap])
                    else:
                        current[buy][cap] = max(prices[i] + after[1][cap - 1], after[0][cap])
            
            # Move to the next index by updating after with current
            after = [row[:] for row in current]
            
        return after[1][2]


       