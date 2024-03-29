class Solution:
    def isUgly(self, n: int) -> bool:
        def uglyNum(n):
            if n == 1:
                return 1
            if n <= 0:
                return 0
            
            if n % 2 == 0:
                return uglyNum(n/2)
            if n % 3 == 0:
                return uglyNum(n/3)
            if n % 5 == 0:
                return uglyNum(n/5)
            return 0
        
        num = uglyNum(n)
        if num == 1:
            return True
        else:
            return False