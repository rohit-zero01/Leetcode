class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)]for _ in range(n)]
        def f(i,amount):
            if i == 0:
                if(amount%coins[0]==0):
                    return 1
                else:
                    return 0

            if dp[i][amount] != -1:
                return dp[i][amount]

            nonTake = 0 + f(i-1, amount)
            Take = 0
            if(coins[i] <= amount):
                Take += f(i, amount - coins[i])

            dp[i][amount] = Take + nonTake
            return dp[i][amount]

        return f(n-1, amount)

        