class Solution:
    def fib(self, n: int) -> int:
        # memo = {}
        # def solve(n):
        #     if n <= 1:
        #         return n

        #     if n in memo:            #MEMOIZATION
        #         return memo[n]

        #     memo[n] = solve(n - 1) + solve(n - 2)
        #     return memo[n]

        # return solve(n)

        # if n <= 1:
        #     return n

        # prev2 = 0
        # prev = 1                   #TABULATION

        # for i in range(2, n + 1):
        #     curr = prev + prev2
        #     prev2 = prev
        #     prev = curr
            
        # return prev

        # if n <= 1:
        #     return n

        # return self.fib(n - 1) + self.fib(n - 2)


        memo = {}
        def f(n):
            if n<=1:
                return n

            if n in memo:
                return memo[n]

            memo[n] = f(n-1) + f(n-2)
            return memo[n]

        return f(n)



















