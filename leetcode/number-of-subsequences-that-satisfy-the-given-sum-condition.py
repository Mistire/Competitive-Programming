class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, res = 0, 0
        right = bisect_right(nums, target - nums[0])
        right = min(right, len(nums)-1)

        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + 2 **(right - left)) % (10**9+7)
                left += 1
            else:
                right -= 1
        return res % (10**9+7)

