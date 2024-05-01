class Solution:
    def findComplement(self, num: int) -> int:
        mask = 0
        comp = ~num

        while num > 0:
            mask = (mask << 1) | 1
            num >>= 1
        res = comp & mask
        return res
            
