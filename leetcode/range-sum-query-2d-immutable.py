class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.preSum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix)+1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.preSum[i][j] = self.preSum[i-1][j] + self.preSum[i][j-1] - self.preSum[i-1][j-1] + matrix[i][j]

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.preSum[r2][c2] - self.preSum[r2][c1 - 1] - self.preSum[r1 - 1][c2] + self.preSum[r1 - 1][c1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)