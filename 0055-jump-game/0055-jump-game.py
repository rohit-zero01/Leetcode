class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxi = 0

        for i in range(len(nums)):
            if i > maxi:
                return False
            maxi = max(maxi, nums[i]+i)

        return True
        