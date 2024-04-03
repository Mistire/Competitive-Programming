class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0      
        direction = [(0,1), (0,-1), (-1,0), (1,0)]
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]

        def inbound(row, col):
            return (0 <= row < len(grid) and (0 <= col < len(grid[0])))

        def dfs(grid, row, col, visited):
            nonlocal count


            visited[row][col] = True

            for rc, cc in direction:
                nr = row + rc
                nc = col + cc

                if (not inbound(nr, nc) and grid[row][col] == 1) or (grid[row][col] == 1 and grid[nr][nc] == 0):
                    count += 1

                if inbound(nr, nc) and not visited[nr][nc]:
                    dfs(grid, nr, nc, visited)

        dfs(grid, 0, 0, visited)
        return count
        
