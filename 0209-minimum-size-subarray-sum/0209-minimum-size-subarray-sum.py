class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        total = 0
        left = 0

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                res = min(right-left+1, res)
                total -= nums[left]
                left += 1
        return res if res != float('inf') else 0