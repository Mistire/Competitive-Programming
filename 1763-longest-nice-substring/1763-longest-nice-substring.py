class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub):
            bitmask_lower = 0
            bitmask_upper = 0
            for char in sub:
                if char.islower():
                    bitmask_lower |= 1 << (ord(char) - ord('a'))
                else:
                    bitmask_upper |= 1 << (ord(char) - ord('A'))
            return bitmask_lower == bitmask_upper

        longest = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if is_nice(substring) and len(substring) > len(longest):
                    longest = substring
        return longest
