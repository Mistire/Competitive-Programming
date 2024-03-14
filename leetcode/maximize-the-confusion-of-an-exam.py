class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        counts = {'T':0,'F':0}
        length = 0

        for right in range(len(answerKey)):
            counts[answerKey[right]] += 1

            while min(counts.values()) > k:
                counts[answerKey[left]] -= 1
                left += 1
            length = max(length, right-left+1)

        return length