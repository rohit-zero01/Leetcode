class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # m = len(grid)
        # n = len(grid[0])
        # dp = [[-1 for _ in range(n)]for _ in range(m)]

        # def f(i,j):
        #     if i == 0 and j == 0:
        #         return grid[0][0]

        #     if i<0 or j<0:
        #         return float('inf')

        #     if dp[i][j] != -1:   #Memoization
        #         return dp[i][j]

        #     up = grid[i][j] + f(i-1,j)
        #     left = grid[i][j] + f(i,j-1)

        #     dp[i][j] = min(up, left)
        #     return dp[i][j]

        # return f(m-1,n-1)

        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m)]for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j ==0:
                    dp[i][j] = grid[i][j]

                else:
                    up = grid[i][j]
                    if i>0:
                        up += dp[i-1][j]
                    else:
                        up += float('inf')
                    
                    left = grid[i][j]
                    if j>0:
                        left += dp[i][j-1]
                    else:
                        left += float('inf')

                    dp[i][j] = min(up, left)

        return dp[n-1][m-1]               

                









