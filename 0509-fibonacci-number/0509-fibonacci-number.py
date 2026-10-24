class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        ans1 = self.fib(n-1)
        ans2 = self.fib(n-2)

        return ans1 + ans2
        