class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        n = len(num)
        count = 0
        
        for i in range(n):
            if i + k <= n:
                d = int(num[i:i+k])
                if d != 0 and int(num) % d == 0:
                    count += 1
        return count
                