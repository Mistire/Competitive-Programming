class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        from typing import List
        def is_magic_square(square):
            # Check if all elements are unique and between 1 and 9
            unique_elements = set()
            for row in square:
                unique_elements.update(row)
            if len(unique_elements) != 9 or not all(1 <= num <= 9 for num in unique_elements):
                return False
            
            # Check sums of rows, columns, and diagonals
            magic_sum = 15
            # Check rows
            for row in square:
                if sum(row) != magic_sum:
                    return False
            # Check columns
            for col in range(3):
                if sum(square[row][col] for row in range(3)) != magic_sum:
                    return False
            # Check diagonals
            if sum(square[i][i] for i in range(3)) != magic_sum:
                return False
            if sum(square[i][2 - i] for i in range(3)) != magic_sum:
                return False
            
            return True
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m - 2):
            for j in range(n - 2):
                square = [grid[i + k][j:j + 3] for k in range(3)]
                if is_magic_square(square):
                    count += 1
        
        return count
