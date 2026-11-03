class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(p)
        m = len(s)
        dp=[[-1 for _ in range(m)]for _ in range(n)]
        # dp = [[-1 for _ in range(m+1)]for _ in range(n+1)]

        def f(i,j):
            if i<0 and j<0:
                return True

            if i<0 and j>=0:
                return False

            if i>=0 and j<0:
                for ii in range(i+1):
                    if p[ii] != '*':
                        return False
                return True

            if dp[i][j] != -1:
                return dp[i][j]

            if p[i] == s[j] or p[i]=="?":
                dp[i][j]= f(i-1,j-1)
                return dp[i][j]

            if p[i] == '*':
                dp[i][j]= f(i-1, j) or f(i, j-1)
                return dp[i][j]
            return False

        return f(n-1, m-1)