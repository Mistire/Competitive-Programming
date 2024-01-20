class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = collections.Counter()
        n = len(nums)
        
        for i in range(n):
            if window[nums[i]] > 0:
                return True
            window[nums[i]] += 1
            
            if i - k >= 0:
                window[nums[i-k]] -= 1
        return False