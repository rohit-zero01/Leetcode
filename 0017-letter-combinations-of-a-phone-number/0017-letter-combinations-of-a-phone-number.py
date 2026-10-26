class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        Pd = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
            }
        res = []

        def backtrack(i, curr):
            if i == len(digits):
                res.append("".join(curr))
                return

            for ch in Pd[int(digits[i])]:
                curr.append(ch)
                backtrack(i+1, curr)
                curr.pop()
        backtrack(0,[])
        return res
            



        