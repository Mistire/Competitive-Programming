class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prSet = set()
        def prime(num):
            d = 2
            while d*d <= num:
                if num % d == 0:
                    prSet.add(d)
                    num //= d
                else:
                    d += 1
            if num > 1:
                prSet.add(num)
            return prSet
        for n in nums:
            prime(n)
        
        return len(prSet)