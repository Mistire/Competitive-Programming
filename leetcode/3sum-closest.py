class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            left, right = i+1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    left += 1
                else:
                    right -= 1
        return res
            


            

