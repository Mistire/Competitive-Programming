class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = []
        mx = 0
        
        for x in nums:
            mx = max(x, mx)
            if len(ans) > 0:
                ans.append(mx+x+ans[-1])
            else:
                ans.append(mx+x)
        return ans