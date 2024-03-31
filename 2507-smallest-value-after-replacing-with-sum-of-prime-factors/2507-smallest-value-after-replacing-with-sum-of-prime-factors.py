class Solution:
    def smallestValue(self, n: int) -> int:
        def primeFactSum(num):
            total = 0
            for i in range(2, ceil(sqrt(num))+1):
                while num % i == 0:
                    total += i
                    num //=i
            if num > 1:
                total += num

            return total

        while True:
            factSum = primeFactSum(n)
            if factSum == n:
                return n
            n = factSum
    
