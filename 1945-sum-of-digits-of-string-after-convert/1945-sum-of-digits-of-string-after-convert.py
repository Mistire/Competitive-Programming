class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_s = []
        for i in range(len(s)):
            num_s.append(str(ord(s[i])-96))
        ss = "".join(num_s)

        tot = 0
        
        while k != 0:
            num = 0
            for i in ss:
                num += int(i)
            tot = num
            ss = str(num)
            k-=1
                
        return tot
        