class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def para(n, open, close, curr, res):
            if open == n and close == n:
                res.append("".join(curr))
                return
            
            if open < n :
                curr.append("(")
                para(n, open+1, close, curr, res)
                curr.pop()

            if close<open:
                curr.append(")")
                para(n, open, close+1, curr, res)
                curr.pop()

        para(n, 0, 0, [], res)
        return res


