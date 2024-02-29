class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = float('-inf')
        windowSum = 0
        
        for i in range(len(nums)):
            windowSum += nums[i]
            if i >= k - 1:
                maxAvg = max(maxAvg, windowSum/k)
                windowSum -= nums[i-k+1]
        return maxAvg