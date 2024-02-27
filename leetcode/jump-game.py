class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # goal = n

        # for i in range(n - 1, -1, -1):
        #     if i + nums[i] >= goal:
        #         goal = i
        # return goal == 0

        max_reach = 0
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True
