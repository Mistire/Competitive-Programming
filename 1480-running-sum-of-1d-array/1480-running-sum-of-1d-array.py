class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        prefix = []

        for i in range(len(nums)):
            sum += nums[i]
            prefix.append(sum)

        return prefix
