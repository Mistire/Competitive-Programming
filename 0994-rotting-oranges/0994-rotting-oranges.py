class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        direction = [(0,1), (0,-1), (-1,0), (1,0)]
        queue = deque([(i,j) for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j] == 2])
        count = 0

        while queue:
            infected = False
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for rc, cc in direction:
                    nr = row + rc
                    nc = col + cc

                    if inbound(nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        infected = True
                        
            if infected:
                count += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return count

