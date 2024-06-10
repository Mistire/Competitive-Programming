class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if exp[i] != heights[i]:
                count += 1
        return count