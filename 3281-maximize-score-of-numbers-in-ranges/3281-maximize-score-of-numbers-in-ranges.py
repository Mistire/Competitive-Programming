class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        def canAchieve(min_diff: int) -> bool:
            prev = start[0]
            for i in range(1, len(start)):
                candidate = prev + min_diff
                if candidate > start[i] + d:
                    return False
                prev = max(candidate, start[i])
            return True

        low, high = 0, d
        while low < high:
            mid = (low + high + 1) // 2
            if canAchieve(mid):
                low = mid
            else:
                high = mid - 1
        
        return low