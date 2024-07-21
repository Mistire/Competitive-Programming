class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        count = Counter(edges)

        return max(count.values()) if max(count.values()) != 1 else -1