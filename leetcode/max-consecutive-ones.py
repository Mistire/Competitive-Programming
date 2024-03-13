class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        length = 0

        for right in range(len(nums)):
            if nums[right] != 1:
                left = right + 1
            length = max(length, right - left + 1)
        return length
