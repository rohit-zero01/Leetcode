class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def combiSum(i, curr):
            if sum(curr) > target:
                return

            if sum(curr) == target:
                res.append(list(curr))
                return

            for d in range(i, len(candidates)):
                curr.append(candidates[d])
                combiSum(d, curr)
                curr.pop()



        combiSum(0,[])
        return res

            
        
        