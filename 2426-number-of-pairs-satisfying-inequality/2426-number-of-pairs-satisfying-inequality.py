from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        res = 0
        sorted_list = SortedList()
        
        for a, b in zip(nums1, nums2):
            target = a - b + diff
            res += sorted_list.bisect_right(target)
            sorted_list.add(a - b)
        
        return res