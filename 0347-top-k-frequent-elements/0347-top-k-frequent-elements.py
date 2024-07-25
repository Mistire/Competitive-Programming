class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        nums_tup = [(val, key) for key, val in nums_count.items()]
        nums_val = heapq.nlargest(k, nums_tup)
        res = [key for (val, key) in nums_val]
        return res