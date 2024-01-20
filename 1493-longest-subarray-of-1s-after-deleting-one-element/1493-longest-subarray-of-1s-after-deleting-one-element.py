class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        numZero = 1
        l =0
        
        for r in range(len(nums)):
            numZero -= nums[r] == 0
            if numZero < 0:
                numZero += nums[l] == 0
                l += 1
        return r - l