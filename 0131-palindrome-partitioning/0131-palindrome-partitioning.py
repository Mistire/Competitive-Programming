class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = {}
        n = len(s)
        def pali(strs):
            if strs == strs[::-1]: 
                return True 
            else: 
                return False
        def dp(i):
            ans = []
            if i == n:
                return [[]]
            
            for j in range(i, n):
                prefix = s[i:j+1]
                if pali(prefix):
                    all_poss = dp(j+1)
                    for poss in all_poss:
                        ans.append([prefix]+poss)
            return ans
        return dp(0)