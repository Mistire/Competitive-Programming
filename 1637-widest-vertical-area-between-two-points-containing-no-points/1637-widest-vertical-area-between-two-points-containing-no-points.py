class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        diff = 0

        for i in range((len(points))):
            if i + 1 < len(points):
                temp = diff
                diff = points[i+1][0] - points[i][0]
            diff = max(diff, temp)

        return diff

        