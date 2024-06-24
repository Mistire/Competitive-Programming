class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = 0
        cnt_ones = 0

        for c in s:
            if c == "1":
                cnt_ones += 1
            else:
                res = min(res+1, cnt_ones)
        return res
