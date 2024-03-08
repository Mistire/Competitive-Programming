class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)

        while left <= right:
            mid = (left+right) // 2
            sumDivs = 0

            for i in range(len(nums)):
                divs = 0
                divs = ceil(nums[i] / mid)
                sumDivs += divs
            if sumDivs > threshold:
                left = mid + 1
            else:
                right = mid - 1

        return left
