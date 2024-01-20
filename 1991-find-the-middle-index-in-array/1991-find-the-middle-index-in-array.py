class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        current = 0
        
        for index in range(n):
            current += nums[index]
            if current - nums[index] == total - current:
                return index
        return -1