#IMP1
import bisect
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # temp = []
        # for x in nums:
        #     if not temp or x > temp[-1]:    #binary search approach, only for 
        #         temp.append(x)                #counting the elements in the LIS
        #     else:
        #         idx = bisect.bisect_left(temp, x)
        #         temp[idx] = x
        # return len(temp)


        n = len(nums)
        dp = [1]*n

        for i in range(n):
            for j in range(i):
                if nums[j]< nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            

        return max(dp)

