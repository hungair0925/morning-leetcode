class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i in range(len(prices)):
            for j in range(len(prices)):
                if i == j:
                    continue
                if i > j:
                    continue
                current_profit = prices[j] - prices[i]

                if profit < current_profit:
                    profit = current_profit

        return profit
