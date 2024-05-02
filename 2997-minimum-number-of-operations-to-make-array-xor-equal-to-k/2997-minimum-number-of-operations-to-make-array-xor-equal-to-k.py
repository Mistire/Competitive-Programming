class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        final_xor = 0
        count = 0

        for n in nums:
            final_xor ^= n
        
        while final_xor or k:
            if (final_xor % 2) != (k % 2):
                count += 1
            final_xor >>= 1
            k >>= 1
        
        return count 
