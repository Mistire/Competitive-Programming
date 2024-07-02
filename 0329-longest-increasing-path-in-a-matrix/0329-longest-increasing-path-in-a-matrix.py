class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 10**10
        @cache
        def dfs(r,c):
    
            best = 1

            if ( -1 < c-1 < COLS) and grid[r][c-1] > grid[r][c]: 
                best= max(best,dfs(r,c-1) + 1)
            if (-1 < c+1 < COLS) and grid[r][c+1] > grid[r][c]: 
                best= max(best,dfs(r,c+1) + 1)
            if (-1 < r-1 < ROWS) and grid[r-1][c] > grid[r][c]: 
                best= max(best,dfs(r-1,c) + 1)
            if (-1 < r+1 < ROWS) and grid[r+1][c] > grid[r][c] : 
                best= max(best,dfs(r+1,c) + 1)
            return best 


        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans,dfs(r,c))
        return ans 
