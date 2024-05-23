class Solution:
    def numSquares(self, n: int) -> int:
        perfect_sq = [i*i for i in range(n) if i*i <= n]
        dp = [n] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for num in perfect_sq:
                if i - num >= 0:
                    dp[i] = min(dp[i],1 + dp[i-num])
        print(dp)
        return dp[-1]