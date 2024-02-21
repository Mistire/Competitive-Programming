class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = set()

        for start, end in ranges:
            for j in range(start , end + 1):
                nums.add(j)
            print(nums)
        
        for i in range(left , right + 1):
            if i not in nums:
                return False
        
        return True