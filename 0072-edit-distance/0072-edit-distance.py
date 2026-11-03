class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        # dp = [[-1 for _ in range(m+1)]for _ in range(n+1)]
        prev = [0] * (m+1)
        curr = [0] * (m+1)


        for j in range(0,m+1):
            prev[j] = j

        # for i in range(0,n+1):
        #     curr[0] = i

        for i in range(1,n+1):
            curr[0] = i
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    curr[j]= prev[j-1]                    
                else:
                    curr[j]= 1 + min(prev[j],min(curr[j-1],prev[j-1]))
            prev = curr.copy()       
        return prev[m]

        # def f(i,j):
        #     if i==0:
        #         return j
        #     if j==0:
        #         return i

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if word1[i-1] == word2[j-1]:
        #         dp[i][j]= f(i-1,j-1)
        #         return dp[i][j]
        #     else:
        #         dp[i][j]= 1 + min(f(i-1,j),min(f(i,j-1),f(i-1,j-1)))
        #         return dp[i][j]
        # return f(n, m)
        