class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Your original linear House Robber logic wrapped in a helper function
        def rob_linear(houses: list[int]) -> int:
            prev = houses[0]
            prev2 = 0

            for i in range(1, len(houses)):
                take = houses[i]
                if i > 1:
                    take += prev2

                not_take = 0 + prev

                cur_i = max(take, not_take)
                prev2 = prev
                prev = cur_i

            return prev

        # Compare robbing from house 0 to n-2 vs house 1 to n-1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))