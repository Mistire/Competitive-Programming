class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]
        if len(nums) == 2:
            return min(nums)
        while left <= right:
            mid = (left+right) // 2

            if nums[mid] > res:
                left = mid + 1
            else:
                res = min(res, nums[mid])
                right = mid - 1
            
        return res
        