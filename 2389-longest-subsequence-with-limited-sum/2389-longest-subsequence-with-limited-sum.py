class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix = [0]
        nums.sort()
        
        for x in nums:
            prefix.append(prefix[-1] + x)
        ans = []
        for q in queries:
            index = bisect.bisect_right(prefix, q)
            ans.append(index-1)
        return ans