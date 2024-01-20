class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        
        # Initialize left sum
        left_sum = 0

        # Iterate through the array to find the pivot index
        for i in range(len(nums)):
            # Check if the sum to the left is equal to the sum to the right
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            # Update the left sum for the next iteration
            left_sum += nums[i]

        # If no pivot index is found, return -1
        return -1