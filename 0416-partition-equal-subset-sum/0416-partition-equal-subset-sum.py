class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t = sum(nums) // 2
        n = len(nums)
        if sum(nums) % 2:
            return False
        memo = [0]* (n)
        def dp(i, t):
            if t <= 0 or i == n:
                return t == 0 
            if memo[i] == 0:
                memo[i] = dp(i+1, t-nums[i]) or dp(i+1, t)
            return memo[i]
        
        return dp(0, t)
        
        
        