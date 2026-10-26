class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def combi(i, curr):
           
            if len(curr)==k:
                res.append(list(curr))
                return
            
            for d in range(i, n - (k - len(curr)) + 2):
                curr.append(d)
                combi(d+1, curr)
                curr.pop()

        combi(1, [])
        return res

            
        