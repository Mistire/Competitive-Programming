class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        n == 2**31-1
        x = 0
        i = 0
        while x <= 2**31:
            print(i)
            i += 1
            x = 3**i
    mx = 19
        """
        mx = 3**19
        
        return n > 0 and mx%n == 0