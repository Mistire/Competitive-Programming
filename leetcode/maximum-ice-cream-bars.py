class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total = 0
        count = 0

        if min(costs) > coins:
            return 0
        if sum(costs) < coins:
            return len(costs)

        for i in range(len(costs)):
            total += costs[i]
            if total <= coins:
                count += 1
        return count

