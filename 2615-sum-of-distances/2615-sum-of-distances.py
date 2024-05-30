class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        num_dict = {i:num for i, num in enumerate(nums)}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    res[i] += abs(i - j)

        return res
            