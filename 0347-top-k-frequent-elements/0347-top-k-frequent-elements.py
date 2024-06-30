class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        num_arr = [(val, key) for key, val in num_count.items()]
        num_large = nlargest(k, num_arr)
        res = [key for val, key in num_large]
        return res