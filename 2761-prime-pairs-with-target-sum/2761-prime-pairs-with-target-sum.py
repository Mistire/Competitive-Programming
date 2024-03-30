class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True] * (n+1)
        prime[0] = prime[1] = False

        for i in range(2, ceil(sqrt(n))):
            if prime:
                j = i*i
                while j <= n:
                    prime[j] = False
                    j += i
        res = []

        for i in range(2, n+1):
            if i + i > n:
                break
            if prime[i] and prime[n-i]:
                res.append([i, n-i])
        return res
        
        


