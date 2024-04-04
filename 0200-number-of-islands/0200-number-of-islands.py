class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        count = 0

        def inbound(row,col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(grid, row, col):
            nonlocal count
            grid[row][col] = '0'

            for rc, cc in direction:
                nr = rc + row
                nc = cc + col

                if inbound(nr, nc) and grid[nr][nc] == '1':
                    dfs(grid, nr, nc)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" :
                    dfs(grid, row, col)
                    count += 1
                
        return count








        






















        