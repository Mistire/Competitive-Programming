class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(day, buy_stock):
            if day >= len(prices):
                return 0
            
            if (day, buy_stock) not in memo:
                if buy_stock == True:
                    sell = prices[day] + dp(day + 1, False)
                    leave = dp(day + 1, True)
                    memo[(day, buy_stock)] = max(sell, leave)
                else:
                    buy = dp(day + 1, True) - prices[day]
                    leave = dp(day + 1, False)
                    memo[(day, buy_stock)] = max(buy, leave)
            
            return memo[(day, buy_stock)]


        return dp(0, False)