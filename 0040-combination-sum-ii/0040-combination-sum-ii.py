class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # res = []
        # seen = set()
        # candidates.sort()

        # def CombiSum2(i,curr, target):
        #     if target == 0:
        #         curr_tuple = tuple(curr)
        #         if curr_tuple not in seen:    Brute force
        #             res.append(list(curr))
        #             seen.add(curr_tuple)
        #         return

        #     if i == len(candidates) or target<0:
        #         return

        #     if candidates[i]<=target:
        #         curr.append(candidates[i])
        #         CombiSum2(i+1,curr, target-candidates[i])
        #         curr.pop()

        #     CombiSum2(i+1,curr, target)
        # CombiSum2(0,[], target)
        # return res
            
        res = []
        candidates.sort()

        def CombiSum2(ind, curr,target) :
            if target == 0:
                res.append(list(curr))

            for i in range(ind, len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                
                curr.append(candidates[i])
                CombiSum2(i+1, curr, target - candidates[i])
                curr.pop()

        CombiSum2(0,[],target)
        return res
            



        