class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)

        while len(stones) > 1:
            smash = heapq._heappop_max(stones) - stones[0]
            if smash:
                heapq._heapreplace_max(stones, smash)
            else:
                heapq._heappop_max(stones)
        stones.append(0)

        return stones[0]