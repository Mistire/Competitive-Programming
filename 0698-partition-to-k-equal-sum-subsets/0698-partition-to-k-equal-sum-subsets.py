class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False
        
        
        target = total // k
        dp = [0] * k

        def backtrack(idx):
            if idx == len(nums):
                return all(num == target for num in dp)
            
            for i in range(k):
                
                if nums[idx] + dp[i] <= target:
                    dp[i] += nums[idx]
                    
                    if backtrack(idx+1):
                        return True
                    dp[i] -= nums[idx]
                if dp[i] == 0: 
                    break
                
            return False

        return backtrack(0)

        
        