class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def sub(i, curr):
            if i == len(nums):
                res.append(list(curr))
                return

            curr.append(nums[i])
            sub(i + 1, curr)
            curr.pop()

            sub(i+1, curr)
        sub(0,[])
        return res


        