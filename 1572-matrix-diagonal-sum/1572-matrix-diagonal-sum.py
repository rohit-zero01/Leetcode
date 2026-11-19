class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total = 0
    
        for i in range(n):
            sec_col = n-1-i
            total += mat[i][i]

            if i!=sec_col:
                total += mat[i][sec_col]

        return total


        