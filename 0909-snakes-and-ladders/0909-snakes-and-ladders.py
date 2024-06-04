class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()

        def inToPos(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r % 2 != 0:
                c = n - 1 - c
            return [r,c]

        queue = deque()
        queue.append([1, 0])
        visit = set()

        while queue:
            square, move = queue.popleft()
            for i in range(1, 7):
                next_square = square + i
                r, c = inToPos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]

                if next_square == n * n:
                    return move + 1
                
                if next_square not in visit:
                    visit.add(next_square)
                    queue.append([next_square, move+1])
        return -1

                