class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        num_c = Counter(nums)

        for i, j in num_c.items():
            if j == 1:
                res.append(i)
        return res