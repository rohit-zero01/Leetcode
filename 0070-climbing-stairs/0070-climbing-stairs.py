class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def Stairs(idx):
            if idx <=1:
                return 1

            if idx in memo:            #MEMOIZATION
                return memo[idx]

            left = Stairs(idx-1)
            right = Stairs(idx-2)

            memo[idx] =  left + right
            return memo[idx]

        return Stairs(n)
         
        
        