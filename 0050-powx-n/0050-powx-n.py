class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if n == 1:
                return x
            if n == 0:
                return 1
            
            if n % 2 == 0:
                return pow(x * x, n//2)
            else:
                return x * pow(x * x, (n-1)//2)

        result = pow(x, abs(n))

        return float(result) if n >= 1 else 1/result