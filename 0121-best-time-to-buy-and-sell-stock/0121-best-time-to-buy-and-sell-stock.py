class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0

        for price in prices:
            if price<lowest:
                lowest = price
            elif price - lowest > profit:
                profit = price -lowest
        return profit





                
                

        