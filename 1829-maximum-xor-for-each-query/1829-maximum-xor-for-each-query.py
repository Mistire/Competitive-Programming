class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_xor = (1 << maximumBit) - 1
        
        xor_result = 0
        result = []
        
        for num in nums:
            xor_result ^= num
            result.append(max_xor ^ xor_result)
        
        return result[::-1]
