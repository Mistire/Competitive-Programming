class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score = [sum(nums)]
        left, right = 0, sum(nums)

        for num in nums:
            if num == 0:
                left += 1
            else:
                right -= 1
            score.append(left+right)
        maxScore = max(score)

        return [i for i in range(len(score)) if score[i] == maxScore]
