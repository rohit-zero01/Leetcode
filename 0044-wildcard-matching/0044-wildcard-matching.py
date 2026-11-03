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



        # n = len(p)
        # m = len(s)
        
        # # Initialize 'prev' row corresponding to an empty pattern (i = 0)
        # prev = [False] * (m + 1)
        # prev[0] = True  # Empty pattern matches empty string
        
        # # Fill the DP row by row
        # for i in range(1, n + 1):
        #     curr = [False] * (m + 1)
            
        #     # Base Case for string j = 0 (empty string matches p[0...i-1] only if all are '*')
        #     flag = True
        #     for ii in range(1, i + 1):
        #         if p[ii - 1] != '*':
        #             flag = False
        #             break
        #     curr[0] = flag
            
        #     # Match characters against the string
        #     for j in range(1, m + 1):
        #         if p[i - 1] == s[j - 1] or p[i - 1] == "?":
        #             curr[j] = prev[j - 1]
        #         elif p[i - 1] == '*':
        #             curr[j] = prev[j] or curr[j - 1]
        #         else:
        #             curr[j] = False
            
        #     # Move curr row to prev row for the next iteration
        #     prev = curr

        # return prev[m]


        n, m = len(p), len(s)
        
        # Only one row needed
        dp = [False] * (m + 1)
        dp[0] = True  # Empty pattern matches empty string
        
        for i in range(1, n + 1):
            # Store dp[j-1] from the previous row before overwriting dp[0]
            prev_diagonal = dp[0]
            
            # Update base case for j = 0
            dp[0] = dp[0] and p[i - 1] == '*'
            
            for j in range(1, m + 1):
                temp = dp[j]  # Save current value to act as prev_diagonal for the next j
                
                if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                    dp[j] = prev_diagonal
                elif p[i - 1] == '*':
                    dp[j] = dp[j] or dp[j - 1]
                else:
                    dp[j] = False
                    
                prev_diagonal = temp  # Update for the next column loop
                
        return dp[m]

