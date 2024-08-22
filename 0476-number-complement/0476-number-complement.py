class Solution:
    def findComplement(self, num: int) -> int:
        mask = 0
        compliment = ~num

        for _ in range(num.bit_length()):
            mask = (mask << 1) | 1   
        res = compliment & mask
        return res
            
