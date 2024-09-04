class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_s = ""
        res = 0

        for i in range(len(s)):
            num_s += str(ord(s[i]) - 96)
        
        while k > 0:
            num_tot = 0
            for strs in num_s:
                num_tot += int(strs)
            res = num_tot
            k -= 1
            num_s = str(num_tot)
        
        return res