class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        
        prev1 = 1
        prev2 = 2
        cur = 0
        
        for i in range(2, n):
            cur = prev1 + prev2
            prev1 = prev2
            prev2 = cur
            
        return cur