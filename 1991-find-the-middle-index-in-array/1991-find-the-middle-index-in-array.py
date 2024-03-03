class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # n = len(nums)
        # total = sum(nums)
        # current = 0
        
        # for index in range(n):
        #     current += nums[index]
        #     if current - nums[index] == total - current:
        #         return index
        # return -1


        total = sum(nums)
        current = 0

        for i in range(len(nums)):
            current += nums[i]
            if current - nums[i] == total - current:
                return i
        return -1








