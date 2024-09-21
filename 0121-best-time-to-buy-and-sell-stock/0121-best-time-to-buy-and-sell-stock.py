class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        max_profit = 0
        buy_price = prices[0]

        while right < len(prices):
            if prices[left] > prices[right]:
                buy_price = prices[right]
                left = right
            else:
                profit = prices[right] - buy_price
                max_profit = max(max_profit, profit)
            right += 1
        return max_profit
            
