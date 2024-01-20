class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = 0
        n = len(garbage)
        for c in "MPG":
            mx = 0
            current = 0
            current += garbage[0].count(c)
            mx = max(current, mx)
            
            for i in range(1, n):
                current += travel[i - 1]
                if c in garbage[i]:
                    current += garbage[i].count(c)
                    mx = max(current, mx)
            total += mx
        return total