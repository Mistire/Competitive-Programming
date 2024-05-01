class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na = int(a, 2)
        nb = int(b, 2)
        s = nb + na
        return bin(s)[2:]
        
        
        
        