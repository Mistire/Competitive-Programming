class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        memo = [0]* (n+1)
        def help(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[1], nums[0])

            if memo[i] == 0:
                memo[i] = max(help(i-1), (nums[i] +help( i-2)))
            return memo[i]
        return help(n)