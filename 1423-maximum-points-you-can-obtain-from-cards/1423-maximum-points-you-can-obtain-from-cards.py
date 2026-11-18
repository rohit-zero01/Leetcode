class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        lsum, rsum, maxSum = 0, 0, 0

        for i in range(k):
            lsum += cardPoints[i]
        maxSum = lsum

        rindex = n-1
        for j in range(k-1, -1, -1):
            lsum -= cardPoints[j]
            rsum += cardPoints[rindex]
            rindex -= 1

            maxSum = max(maxSum, lsum + rsum)

        return maxSum




        