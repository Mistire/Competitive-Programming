class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(day, buy_stock):
            if day >= len(prices):
                return 0
            
            if (day, buy_stock) not in memo:
                if buy_stock == True:
                    memo[(day, buy_stock)] = max((prices[day] + dp(day + 1, False)), dp(day + 1, True))
                else:
                    memo[(day, buy_stock)] = max(dp(day + 1, True) - prices[day], dp(day + 1, False))
            
            return memo[(day, buy_stock)]


        return dp(0, False)