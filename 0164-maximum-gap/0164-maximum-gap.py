class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_gap = 0

        if len(nums) < 2:
            return 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, (nums[i] - nums[i-1]))
        return max_gap