class Solution:
    def maxScore(self, cards: List[int], k: int) -> int:
        left = 0
        right = len(cards) - k
        total = sum(cards[right:])
        res = total

        while right < len(cards):
            total += cards[left] - cards[right]
            res = max(res, total)
            left += 1
            right += 1
        return res
