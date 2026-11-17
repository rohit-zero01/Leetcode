
#IMP2
# class Solution:
#     def lengthOfLIS(self, nums: list[int]) -> int:

#         n = len(nums)
#         dp = [1] * n

#         maxi = 1
#         for i in range(n):
#             for prev in range(i):
#                 if nums[prev]< nums[i]:
#                     dp[i] = max(dp[i], 1+dp[prev])
            
#             maxi = max(maxi, dp[i])

#         return maxi


#IMP1
import bisect
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        temp = []
        for x in nums:
            if not temp or x > temp[-1]:
                temp.append(x)
            else:
                idx = bisect.bisect_left(temp, x)
                temp[idx] = x
        return len(temp)



# class Solution:
#     def lengthOfLIS(self, nums: list[int]) -> int:
#         n = len(nums)
#         next_row = [0] * (n + 1)
        
#         for i in range(n - 1, -1, -1):
#             curr_row = [0] * (n + 1)
#             for prev in range(i - 1, -2, -1):
#                 exclude = next_row[prev + 1]
                
#                 include = 0
#                 if prev == -1 or nums[i] > nums[prev]:
#                     include = 1 + next_row[i + 1]
                
#                 curr_row[prev + 1] = max(include, exclude)
                
#             next_row = curr_row
            
#         return next_row[0]
      








# class Solution:
#     def lengthOfLIS(self, nums: list[int]) -> int:
#         n = len(nums)
#         # dp[i][prev + 1] stores the LIS length starting at index i with previous index prev
#         dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
#         for i in range(n - 1, -1, -1):
#             for prev in range(i - 1, -2, -1):
#                 exclude = dp[i + 1][prev + 1]
                
#                 include = 0
#                 if prev == -1 or nums[i] > nums[prev]:
#                     include = 1 + dp[i + 1][i + 1]
                
#                 dp[i][prev + 1] = max(include, exclude)
                
#         return dp[0][0]







