# class Solution:
#     def change(self, amount: int, coins: list[int]) -> int:
        # n = len(coins)
        # dp = [[-1 for _ in range(amount + 1)]for _ in range(n)]
        # def f(i,amount):
        #     if i == 0:
        #         if(amount%coins[0]==0):
        #             return 1
        #         else:
        #             return 0

        #     if dp[i][amount] != -1:   #MEMOIZATION
        #         return dp[i][amount]

        #     nonTake = 0 + f(i-1, amount)
        #     Take = 0
        #     if(coins[i] <= amount):
        #         Take += f(i, amount - coins[i])

        #     dp[i][amount] = Take + nonTake
        #     return dp[i][amount]

        # return f(n-1, amount)
# class Solution:
#     def change(self, amount: int, coins: list[int]) -> int:
#         n = len(coins)
#         dp = [[0 for _ in range(amount + 1)]for _ in range(n)]

#         for a in range(amount+1):
#             if a % coins[0] == 0:
#                 dp[0][a] = 1
#             else:
#                 dp[0][a] = 0

#         for i in range(1,n):
#             for a in range(amount+1):   #TABULATION
#                 nonTake = dp[i-1][a]
#                 Take = 0
#                 if(coins[i] <= a):
#                     Take += dp[i][a - coins[i]]

#                 dp[i][a] = Take + nonTake

#         return dp[n-1][amount]

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        # dp = [[0 for _ in range(amount + 1)]for _ in range(n)]
        prev = [0 for _ in range(amount+1)]
        curr = [0 for _ in range(amount+1)]
        for a in range(amount+1):
            if a % coins[0] == 0:
                prev[a] = 1
            else:
                prev[a] = 0

        for i in range(1,n):
            for a in range(amount+1):
                nonTake = prev[a]
                Take = 0
                if(coins[i] <= a):
                    Take += curr[a - coins[i]]

                curr[a] = Take + nonTake
            prev = curr
        return prev[amount]

        