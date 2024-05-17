class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n+1)] * (m+1)
        dp[0][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j+1] = 1
        for i in range(m):
            for j in range(n):
                dp[i+1][j] = 1

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1] 
        
        return dp[m-1][n-1]
        