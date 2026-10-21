class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums)-1
        # ans = nums[0]

        while low<high:
            guess = (low+high)//2

            if nums[guess]>nums[high]:
                low = guess + 1
            else:
                # ans = nums[guess]
                high = guess

        return nums[low]
        