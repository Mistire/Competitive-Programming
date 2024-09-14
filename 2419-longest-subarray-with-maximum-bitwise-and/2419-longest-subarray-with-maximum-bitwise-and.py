class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, count = 0, 0
        max_num = max(nums)

        for i in range(len(nums)):
            if nums[i] == max_num:
                count += 1
            else:
                count = 0
            res = max(res, count)
        
        return res