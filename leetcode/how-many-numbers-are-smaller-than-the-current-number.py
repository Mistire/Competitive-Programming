class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        count = [0] * 101

        for i in nums:
            count[i] += 1
        for num in nums:
            res.append(sum(count[:num]))
        return res



        
