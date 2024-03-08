class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right= -1, citations[-1] + 1
        size = len(citations)

        while left <= right:
            mid = (right+left) // 2
            index = bisect_right(citations, mid)
            value = size - index

            if value == mid:
                return mid
            if value < mid:
                right = mid - 1
            else:
                left = mid + 1

        return left