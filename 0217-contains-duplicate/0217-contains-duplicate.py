class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_count = Counter(nums)
        return max(nums_count.values()) > 1