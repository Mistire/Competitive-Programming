class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0

        for i in range(1, len(s)):
            if s[i] != s[i-1] and k > 0:
                count += 1
                k -= 1
            elif k == 0:
                return i + 1
        return len(s)


            