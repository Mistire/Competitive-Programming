class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(day, transactions_left, buy_stock):
            if day >= len(prices) or transactions_left == 0:
                return 0
            if (day, transactions_left, buy_stock) in memo:
                return memo[(day, transactions_left, buy_stock)]
            
            if buy_stock == True:
                sell = prices[day] + dp(day+1, transactions_left-1, False)
                leave = dp(day+1, transactions_left, True)
                memo[(day, transactions_left, buy_stock)] = max(sell, leave)
            else:
                buy = dp(day+1, transactions_left, True) - prices[day]
                leave = dp(day+1, transactions_left, False)
                memo[(day, transactions_left, buy_stock)] = max(buy, leave)
            return memo[(day, transactions_left, buy_stock)]
        
        return dp(0, 2, False)
            