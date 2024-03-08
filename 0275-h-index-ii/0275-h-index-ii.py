class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = -1
        right = citations[-1] + 1
        size = len(citations)
        while left + 1 < right:
            mid = (right+left) // 2
            index = bisect_right(citations, mid)
            value = size - index

            if value == mid:
                return mid
            if value < mid:
                right = mid
            else:
                left = mid
        return right