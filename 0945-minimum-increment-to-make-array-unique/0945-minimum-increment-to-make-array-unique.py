class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        num_tracker = 0
        min_increment = 0

        for num in nums:
            num_tracker = max(num, num_tracker)
            min_increment += num_tracker - num
            num_tracker += 1
        return min_increment