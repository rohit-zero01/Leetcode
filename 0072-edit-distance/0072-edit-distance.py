class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[-1 for _ in range(m)]for _ in range(n)]

        def f(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j]= f(i-1,j-1)
                return dp[i][j]
            else:
                dp[i][j]= 1 + min(f(i-1,j),min(f(i,j-1),f(i-1,j-1)))
                return dp[i][j]
        return f(n-1, m-1)
        