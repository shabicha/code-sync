class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minP = prices[0]
        maxP = 0

        for i in range(len(prices)):
            #find/set min
            if prices[i] < minP:
                minP = prices[i]
            elif prices[i]>=minP:
                maxP = max(maxP, prices[i] - minP)
        return maxP