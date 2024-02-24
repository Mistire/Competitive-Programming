class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l, r = 0, 1
        n = len(nums)

        # while r < n:
        #     if nums[l] == nums[r]:
        #         nums.pop(l)
        #         n -= 1
        #     else:
        #         l = r
        #         r += 1
        # return n
        nums[:] = sorted(set(nums))
        return n


        