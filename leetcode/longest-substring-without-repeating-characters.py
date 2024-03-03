class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        charDict = {}

        for R, ch in enumerate(s):
            if ch in charDict and charDict[ch] >= L:
                L = charDict[ch] + 1
            charDict[ch] = R
            length = max(length, R-L+1)
        return length
            