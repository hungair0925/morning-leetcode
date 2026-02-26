class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_buy_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            current_stock_price = prices[i]
            if current_stock_price < min_buy_price:
                min_buy_price = current_stock_price

            current_profit = current_stock_price - min_buy_price
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
