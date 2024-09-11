class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            if nums[i-1] + 1 == nums[i]:
                count += 1
        return count