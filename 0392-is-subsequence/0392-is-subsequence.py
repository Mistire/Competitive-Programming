class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [-1]
        for i in range(len(s)):
            for j in range(dp[-1] + 1 ,len(t)):
                if s[i] == t[j]:
                    dp.append(j)
                    break
            else:
                return False
        return True
        
        
    