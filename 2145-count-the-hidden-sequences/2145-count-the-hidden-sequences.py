class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mn = 0
        mx = 0
        current = 0
        
        for x in differences:
            current += x
            mn = min(mn, current)
            mx = max(mx, current)
        return max((upper - lower) - (mx - mn) + 1, 0)