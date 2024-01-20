class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub):
            return all(c.swapcase() in sub for c in sub)

        max_length = 0
        result = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                current_substring = s[i:j]
                if is_nice(current_substring) and len(current_substring) > max_length:
                    max_length = len(current_substring)
                    result = current_substring

        return result 