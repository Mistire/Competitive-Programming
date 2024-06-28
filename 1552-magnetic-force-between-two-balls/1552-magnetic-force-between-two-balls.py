class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        nums = []
        position.sort()
        nums.append(position[0])
        nums.append(position[-1])

        if m == len(nums):
            return position[-1] - position[0]

        left = position[0]
        right = position[-1]

        while left <= right and len(nums) != m:
            mid = (left+right) // 2
            if m < mid:
                nums.append(mid)
            elif m > mid:
                left = mid + 1
            else:
                right = mid -1
        nums.sort()
        print(nums)
        return nums[1] - nums[0]



    

