class Solution:
    def partitionString(self, s: str) -> int:
        ch_count = defaultdict(int)
        left = 0
        right = 0
        part = 0

        while right < len(s):
            if ch_count[s[right]] == 0:
                ch_count[s[right]] += 1
                right += 1 
            else:
                ch_count = defaultdict(int)
                part += 1
                left = right
        if right > left:
            part += 1
        return part