class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = [0]
        for x in nums:
            prefix.append(x + prefix[-1])
        suffix = [0]
        for x in nums[::-1]:
            suffix.append(x+suffix[-1])
        suffix.reverse()
        answer = [0] * len(nums)
        for i in range(len(nums)):
            answer[i] = abs(prefix[i] - suffix[i+1])
        return answer