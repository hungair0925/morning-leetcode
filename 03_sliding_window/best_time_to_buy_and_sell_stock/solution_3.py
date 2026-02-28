class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        left_buy_index = 0
        right_sell_index = 1

        while right_sell_index < len(prices):
            if prices[left_buy_index] > prices[right_sell_index]:
                left_buy_index = right_sell_index

            current_profit = prices[right_sell_index] - prices[left_buy_index]
            if current_profit > profit:
                profit = current_profit

            right_sell_index += 1

        return profit
