class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 1:
            return 0
        MIN = prices[0]
        profit = 0
        maxProfit = 0
        for i in range(1, length):
            MIN = min(MIN, prices[i-1])
            profit = prices[i] - MIN
            maxProfit = max(maxProfit, profit)
        return maxProfit