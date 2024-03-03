class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # numZero = 1
        # l =0
        
        # for r in range(len(nums)):
        #     numZero -= nums[r] == 0
        #     if numZero < 0:
        #         numZero += nums[l] == 0
        #         l += 1
        # return r - l

        L = 0
        numZero = 1

        for R in range(len(nums)):
            numZero -= nums[R] == 0
            if numZero < 0:
                numZero += nums[L] == 0
                L += 1
        return R - L
















