class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if n<=1:
            return
        
        k = k%n 
        def rev(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
                right -=1

        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)

        


        