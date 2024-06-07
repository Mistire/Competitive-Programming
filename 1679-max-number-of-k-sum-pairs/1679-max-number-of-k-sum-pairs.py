class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        s, e = 0, len(nums) - 1
        operations = 0
        
        while s < e:
            if nums[s] + nums[e] == k:
                operations += 1
                s += 1
                e -= 1
            elif nums[s] + nums[e] > k:
                e -= 1
            else:
                s += 1
        return operations