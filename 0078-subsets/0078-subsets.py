class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backTrack(i, subset):
            if i >= len(nums):
                return res.append(subset[:])

            subset.append(nums[i])
            backTrack(i+1, subset)

            subset.pop()
            backTrack(i+1, subset)

        backTrack(0, [])
        return res



            