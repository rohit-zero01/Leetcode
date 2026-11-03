class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # n = len(p)
        # m = len(s)
        # dp=[[False for _ in range(m+1)]for _ in range(n+1)]
        # # dp = [[-1 for _ in range(m+1)]for _ in range(n+1)]

        # def f(i,j):
        #     if i==0 and j==0:
        #         return True

        #     if i==0 and j>0:
        #         return False

        #     if i>0 and j==0:
        #         for ii in range(1,i+1):
        #             if p[ii-1] != '*':
        #                 return False
        #         return True

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if p[i-1] == s[j-1] or p[i-1]=="?":
        #         dp[i][j]= f(i-1,j-1)
        #         return dp[i][j]

        #     if p[i-1] == '*':
        #         dp[i][j]= f(i-1, j) or f(i, j-1)
        #         return dp[i][j]
        #     return False

        # return f(n, m)

        # n = len(p)
        # m = len(s)
        # # dp=[[False for _ in range(m+1)]for _ in range(n+1)]

        # dp[0][0] = True
        # for j in range(1,m+1):
        #     dp[0][j] = False

        # for i in range(1,n+1):
        #     flag = True
        #     for ii in range(1,i+1):
        #             if p[ii-1] != '*':
        #                 flag = False
        #                 break
        #     dp[i][0] = flag

        #     for i in range(1,n+1):
        #         for i in range(1,m+1):
        #             if p[i-1] == s[j-1] or p[i-1]=="?":
        #                 dp[i][j]= f(i-1,j-1)
        #                 return dp[i][j]

        #             else p[i-1] == '*':
        #                 dp[i][j]= f(i-1, j) or f(i, j-1)
        #                 return dp[i][j]

        #             return False


        n = len(p)
        m = len(s)
        
        # 1. Initialize the DP table with False (+1 size for empty string boundaries)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        # 2. Base case: Both empty pattern and empty string match
        dp[0][0] = True
        
        # 3. Base case: Empty pattern cannot match a non-empty string
        for j in range(1, m + 1):
            dp[0][j] = False

        # 4. Base case: Check if pattern containing only '*' can match empty string
        for i in range(1, n + 1):
            flag = True
            for ii in range(1, i + 1):
                if p[ii - 1] != '*':
                    flag = False
                    break
            dp[i][0] = flag

        # 5. Fill the DP table iteratively
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If characters match or there is a '?' wildcard
                if p[i - 1] == s[j - 1] or p[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]

                # If there is a '*' wildcard
                elif p[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

                # If characters do not match
                else:
                    dp[i][j] = False

        # 6. Return the final cell containing the complete result
        return dp[n][m]