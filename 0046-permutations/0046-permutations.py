class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # res = []

        # def Permu(depth, curr):
        #     if depth == len(nums):
        #         res.append(list(curr))                
        #         return

        #     for i in range(len(nums)):
        #         if nums[i] in curr:
        #             continue

        #         curr.append(nums[i])
        #         Permu(depth + 1, curr)
        #         curr.pop()

        # Permu(0,[])
        # return res

        def backtrack(idx):
            if idx == len(nums):
                result.append(nums[:])
                return

            # Swap current element with every element from index to end
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]  # Swap
                backtrack(idx + 1)                         # Recurse
                nums[idx], nums[i] = nums[i], nums[idx]  # Backtrack (re-swap)

        result = []
        backtrack(0)
        return result
