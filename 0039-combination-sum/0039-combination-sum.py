class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def CombiSum(i, curr, target):
            if target == 0:
                res.append(list(curr))
                return
        
            # Base case 2: Out of bounds or target exceeded
            if i == len(candidates) or target < 0:
                return

            if candidates[i]<=target:
                curr.append(candidates[i])
                CombiSum(i, curr, target-candidates[i])
                curr.pop()

            CombiSum(i+1, curr, target)

        CombiSum(0,[], target)
        return res










            
        
        