class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        lCount = rCount = added = 0
        
        for char in s:
            if char == "(":
                lCount += 1
            else:
                if rCount < lCount:
                    rCount += 1
                else:
                    added += 1
        added += lCount - rCount
        return added