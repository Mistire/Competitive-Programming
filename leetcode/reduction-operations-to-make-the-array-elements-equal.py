class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
               res += i+1 
        return res
