class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        prev = [0]*m
        curr = [0]*m

        for j in range(m):
            prev[j] = matrix[0][j]

        # Fill the DP table
        for i in range(1, n):
            for j in range(m):
                # Option 1: Move straight up
                u = matrix[i][j] + prev[j]
                
                # Option 2: Move diagonal left
                ld = 1e9
                if j - 1 >= 0:
                    ld = matrix[i][j] + prev[j-1]
                    
                # Option 3: Move diagonal right
                rd = 1e9
                if j + 1 < m:
                    rd = matrix[i][j] + prev[j+1]
                    
                curr[j] = min(u, ld, rd)
            prev = list(curr)
        return min(prev)   
   