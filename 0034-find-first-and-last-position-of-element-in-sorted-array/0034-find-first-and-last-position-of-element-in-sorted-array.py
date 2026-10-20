class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low = 0
        high = len(nums)-1
        ans = [-1, -1]

        while low<=high:
            guess = (low+high)//2

            if nums[guess] > target:
                high = guess -1
            elif nums[guess] < target:
                low = guess + 1
            else:
                ans[0] = guess
                high = guess - 1

        # Reset pointers for the second search
        low = 0
        high = len(nums) - 1

        while low <= high:
            guess = (low + high) // 2
            
            if nums[guess] > target:
                high = guess - 1
            elif nums[guess] < target:
                low = guess + 1
            else:
                ans[1] = guess       # Record the index as the last position
                low = guess + 1      # Continue searching right for a later occurrence
        
        return ans

        