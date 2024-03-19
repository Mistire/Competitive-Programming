class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        count = float('inf')
        cardCount = defaultdict(int)

        for right in range(len(cards)):
            cardCount[cards[right]] += 1
            while cardCount[cards[right]] == 2 and left < len(cards):
                count = min(count, right-left+1)
                cardCount[cards[left]] -= 1
                if cardCount[cards[left]] == 0:
                    del cardCount[cards[left]]
                left += 1
                
        return count if count != float('inf') else -1