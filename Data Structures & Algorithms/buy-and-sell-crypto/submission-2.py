class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1
        while l < len(prices) and r < len(prices):
            max_profit = max(max_profit, prices[r]-prices[l])
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1

        return max_profit
            