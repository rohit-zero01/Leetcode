class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n)]for _ in range(m)]

        def f(i,j):
            if(i<0 or j<0):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if(text1[i]==text2[j]):
                return 1+ f(i-1,j-1)

            dp[i][j] =  max(f(i-1,j),f(i,j-1))
            return  dp[i][j] 

        return f(m-1,n-1)
        