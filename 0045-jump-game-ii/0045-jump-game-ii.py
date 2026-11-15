# class Solution:
#     def jump(self, nums: list[int]) -> int:
        
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def solve(i):
            if i >= n - 1:
                return 0

            if dp[i] != -1:
                return dp[i]

            ans = float('inf')

            for j in range(1, nums[i] + 1):
                ans = min(ans, 1 + solve(i + j))

            dp[i] = ans
            return dp[i]

        return solve(0)






