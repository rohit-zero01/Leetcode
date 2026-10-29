class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def rob_linear(houses: list[int]) -> int:
            prev = 0
            curr = 0
            for money in houses:
                temp = max(curr, prev + money)
                prev = curr
                curr = temp
            return curr

        # Compare robbing (from house 0 to n-2) vs (from house 1 to n-1)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))