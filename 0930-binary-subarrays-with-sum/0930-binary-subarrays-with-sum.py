class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_count = {0: 1}
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in prefix_count:
                count += prefix_count[prefix_sum - goal]
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1
        
        return count
             