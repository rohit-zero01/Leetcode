class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # res = []
        # def combiSum(i, curr):
        #     if sum(curr) > target:
        #         return

        #     if sum(curr) == target:
        #         res.append(list(curr))
        #         return

        #     for d in range(i, len(candidates)):
        #         curr.append(candidates[d])
        #         combiSum(d, curr)
        #         curr.pop()



        # combiSum(0,[])
        # return res
        res = []

        def combiSum(i, curr, total):
            # Base Case 1: Target reached
            if total == target:
                res.append(list(curr))
                return
            
            # Base Case 2: Out of bounds or exceeded target
            if i >= len(candidates) or total > target:
                return

            # Choice 1: Include candidates[i] (stay at index 'i' to allow reuse)
            curr.append(candidates[i])
            combiSum(i, curr, total + candidates[i])
            
            # Backtrack
            curr.pop()

            # Choice 2: Skip candidates[i] and move to the next index
            combiSum(i + 1, curr, total)

        # Start recursion with index 0 and initial total of 0
        combiSum(0, [], 0)
        return res

            
        
        