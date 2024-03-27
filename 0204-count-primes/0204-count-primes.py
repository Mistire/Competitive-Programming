class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        prime = [True for _ in range(n)]
        prime[0] = prime[1] = False
        i = 2
        while i*i <n:

            if prime:
                j = i*i

                while j < n:
                    prime[j] = False

                    j += i
            i += 1
        res = Counter(prime)
        for num,val in res.items():
            if num :
                return val
        
       

