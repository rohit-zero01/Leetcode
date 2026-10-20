class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low<=high:
            guess = (low+high)//2

            if nums[guess] > target:
                high = guess - 1            
            elif nums[guess] < target:
                low = guess + 1
            else:
                return guess

        return -1


        