class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            left, right = 0, len(matrix[0]) - 1
            while left <= right:
                mid = (left+right) // 2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            i += 1
        return False
