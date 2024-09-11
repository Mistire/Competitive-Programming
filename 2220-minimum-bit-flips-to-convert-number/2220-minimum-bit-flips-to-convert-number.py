class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while (start != 0 or goal != 0):
            s_bit = start & 1
            g_bit = goal & 1

            if s_bit != g_bit:
                count += 1
            start >>= 1
            goal >>= 1
        return count