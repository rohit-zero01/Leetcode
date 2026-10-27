class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def Permu(depth, curr):
            if depth == len(nums):
                res.append(list(curr))                
                return

            for i in range(len(nums)):
                if nums[i] in curr:
                    continue

                curr.append(nums[i])
                Permu(depth + 1, curr)
                curr.pop()

        Permu(0,[])
        return res
                


        