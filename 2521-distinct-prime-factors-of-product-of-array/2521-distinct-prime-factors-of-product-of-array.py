class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = reduce((lambda x, y: x * y), nums)
        def prime(num):
            prSet = set()
            d = 2
            while d*d <= num:
                while num % d == 0:
                    prSet.add(d)
                    num //= d
                else:
                    d += 1
            if num > 1:
                prSet.add(num)
            return prSet
        return len(prime(res))