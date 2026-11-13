class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i, j = 0, 0
        while i < len(prices) and j < len(prices):
            j += 1
            while j < len(prices) and prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i])
                j += 1
            i = j

        return max_profit