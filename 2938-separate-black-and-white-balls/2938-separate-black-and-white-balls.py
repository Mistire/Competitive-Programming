class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = 0
        res = 0

        for strs in s:
            if strs == "1":
                ones += 1
            else:
                res += ones 
        return res