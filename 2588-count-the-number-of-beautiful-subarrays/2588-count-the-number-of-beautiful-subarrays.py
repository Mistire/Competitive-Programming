class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        seen = collections.Counter()
        current = 0
        count = 0
        
        seen[current] += 1
        for x in nums:
            current ^= x
            count += seen[current]
            seen[current] += 1
        return count