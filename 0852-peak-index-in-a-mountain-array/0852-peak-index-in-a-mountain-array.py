class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        low = 0
        high = len(arr)-1

        while low<high:
            guess = (low+high)//2

            if arr[guess+1]> arr[guess]:
                low = guess+1
            else:
                ans = guess
                high = guess 
        return ans

        