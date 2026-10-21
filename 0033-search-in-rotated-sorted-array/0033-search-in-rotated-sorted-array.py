class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        ans = -1

        while low<=high:
            guess = (low+high)//2

            if nums[guess] == target:
                ans = guess
                break

            if nums[low]<=nums[guess]:
                if nums[low]<=target<=nums[guess]:
                    high = guess - 1
                else:
                    low = guess + 1
            else:
                if nums[guess] < target <= nums[high]:
                    low = guess + 1
                else:
                    high = guess - 1
            
        return ans
        
        

            
        