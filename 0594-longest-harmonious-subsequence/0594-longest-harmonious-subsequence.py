class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        return max([v+c[k+1] for k, v in c.items() if k+1 in c] + [0])