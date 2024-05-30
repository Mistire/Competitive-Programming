class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False] * (n+1) for i in range(n)]
        dp[0][0] = True

        for i in range(1, n):
            for j in range(i):
                k = stones[i] - stones[j]
                if k <= j+1 and (dp[j][k-1] or dp[j][k] or dp[j][k+1]):
                    dp[i][k] = True
                    if i == n-1:
                        return True
        return False
