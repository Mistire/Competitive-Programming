class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        nums.sort()
        count = 0
        while l < r:
            if nums[l] + nums[r] >= target:
                r -= 1
            elif nums[l] + nums[r] < target:
                count += r - l
                l += 1
        return count
                
