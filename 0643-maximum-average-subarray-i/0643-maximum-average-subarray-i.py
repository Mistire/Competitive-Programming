class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = float('-inf')
        total = 0
        left = 0

        for right in range(len(nums)):
            total += nums[right]
            if right - left + 1 == k:
                maxAvg = max((total/k), maxAvg)
                total -= nums[left]
                left += 1

        return maxAvg


        

        








