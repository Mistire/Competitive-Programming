class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Calculate the prefix sum from left to right
        prefix_sum_left = [0] * n
        prefix_sum_left[0] = nums[0]
        for i in range(1, n):
            prefix_sum_left[i] = prefix_sum_left[i - 1] + nums[i]

        # Calculate the prefix sum from right to left
        prefix_sum_right = [0] * n
        prefix_sum_right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            prefix_sum_right[i] = prefix_sum_right[i + 1] + nums[i]

        # Calculate the absolute differences between left and right sums
        differences = [abs(prefix_sum_left[i] - prefix_sum_right[i]) for i in range(n)]

        return differences