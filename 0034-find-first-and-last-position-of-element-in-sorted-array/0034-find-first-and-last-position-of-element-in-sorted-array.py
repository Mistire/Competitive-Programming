class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # def binarySearchLeft(num, target):
        #     lo, hi = 0, len(nums) - 1

        #     while lo <= hi:
        #         mid = (lo+hi) // 2
        #         if nums[mid] < target:
        #             lo = mid + 1
        #         else:
        #             hi = mid - 1
        #     return lo

        # def binarySearchRight(num, target):
        #     lo, hi = 0, len(nums) - 1

        #     while lo <= hi:
        #         mid = (lo+hi) // 2
        #         if nums[mid] <= target:
        #             lo = mid + 1
        #         else:
        #             hi = mid - 1
        #     return hi

        left = bisect.bisect_left(nums,target)
        right = bisect.bisect_right(nums, target)

        if left < len(nums) and nums[left] == target:
            return [left, right-1]
        else:
            return [-1, -1]



