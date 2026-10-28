class Solution:
    def fib(self, n: int) -> int:
        # memo = {}
        # def solve(n):
        #     if n <= 1:
        #         return n

        #     if n in memo:
        #         return memo[n]

        #     memo[n] = solve(n - 1) + solve(n - 2)
        #     return memo[n]

        # return solve(n)

        if n <= 1:
            return n

        prev2 = 0
        prev = 1

        for i in range(2, n + 1):
            curr = prev + prev2
            prev2 = prev
            prev = curr
            
        return prev

        # if n <= 1:
        #     return n

        # return self.fib(n - 1) + self.fib(n - 2)