class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # l = 0
        # for r,n in enumerate(nums):
        #     k -= (1-n)
        #     if k < 0:
        #         k += (1-nums[l])
        #         l += 1
        # return r-l+1

        L = 0
        for R, n in enumerate(nums):
            k -= (1 - n)
            if k < 0:
                k += (1 - nums[L])
                L += 1
        return R - L + 1








