class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(len(prices)):
                if i < j:
                    tmp_profit = prices[j] - prices[i]
                    if tmp_profit > max_profit:
                        max_profit = tmp_profit
        return max_profit