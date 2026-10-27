# class Solution:
#     def permute(self, nums: list[int]) -> list[list[int]]:
#         res = []

#         def Permu(depth, curr):
#             if depth == len(nums):
#                 res.append(list(curr))                
#                 return

#             for i in range(len(nums)):
#                 if nums[i] in curr:
#                     continue

#                 curr.append(nums[i])
#                 Permu(depth + 1, curr)
#                 curr.pop()

#         Permu(0,[])
#         return res
                
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def Permu(depth):
            if depth == len(nums):
                res.append(list(nums)) # nums itself becomes the permutation!
                return

            # Notice the loop starts from 'depth' now
            for i in range(depth, len(nums)):
                # Swap to place nums[i] at the current depth position
                nums[depth], nums[i] = nums[i], nums[depth]
                
                Permu(depth + 1)
                
                # Backtrack: Swap them back to their original spots
                nums[depth], nums[i] = nums[i], nums[depth]

        Permu(0)
        return res


        