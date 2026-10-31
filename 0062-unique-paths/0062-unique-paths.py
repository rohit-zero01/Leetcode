class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[-1 for _ in range(n)]for _ in range(m)]
        # def f(i,j,dp):
        #     if i == 0 and j == 0:
        #         return 1

        #     if i<0 or j<0:
        #         return 0

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     up = f(i-1,j,dp)
        #     left = f(i,j-1,dp)

        #     dp[i][j] = up + left
        #     return dp[i][j]
        # return f(m-1,n-1, dp)


        # Create a 1D DP array of size n initialized to 1, 
        # representing the previous row's path counts.
        dp = [1] * n
        
        # Iterate for each row starting from the second row up to m-1
        for _ in range(1, m):
            for j in range(1, n):
                # dp[j] currently holds the value from the previous row (top),
                # and dp[j-1] holds the updated value from the current row (left).
                dp[j] = dp[j] + dp[j-1]
                
        # For a 1x1 grid, the loops won't run and it returns dp[0] which is 1.
        return dp[n - 1]
        