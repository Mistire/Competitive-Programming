class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 0
        charDict = {}

        for right, char in enumerate(s):
            while char in charDict and charDict[char] >= left:
                left = charDict[char] + 1
            charDict[char] = right
            length = max(length, right - left + 1)
        return length
            