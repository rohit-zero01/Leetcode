class Solution:
    def rob(self, nums: list[int]) -> int:
        prev = nums[0]
        prev2 = 0

        for i in range(1, len(nums)):
            take = nums[i]
            if i >1:
                take += prev2

            not_take = 0 + prev

            cur_i = max(take, not_take)
            prev2 = prev
            prev = cur_i

        return prev
        
        