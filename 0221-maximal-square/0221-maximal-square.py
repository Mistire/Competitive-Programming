class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_ones = 0
        row = len(matrix)
        col = len(matrix[0])
        if matrix.count("1") >= col * row:
            return 1

        for i in range(row):
            row_ones = 0
            for j in range(col):
                if matrix[i][j] == "1":
                    row_ones += 1
            max_ones = max(max_ones, row_ones)
            temp = sqrt(max_ones)
            if temp == (temp//1):
                return max_ones

        return 1
        