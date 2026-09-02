class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        selling_value = prices[0]

        for i in prices:
            if i < selling_value:
                selling_value = i
                continue
            tmp_profit = i - selling_value
            if tmp_profit > max_profit:
                max_profit = tmp_profit
        return max_profit