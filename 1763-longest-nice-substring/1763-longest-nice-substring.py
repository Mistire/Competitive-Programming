class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub):
            bitmsk_lower = 0
            bitmsk_upper = 0
            for char in sub:
                if char.islower():
                    bitmsk_lower |= 1 << (ord(char) - ord('a'))
                else:
                    bitmsk_upper |= 1 << (ord(char) - ord('A'))
            return bitmsk_lower == bitmsk_upper

        longest = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if is_nice(substring) and len(substring) > len(longest):
                    longest = substring
        return longest
