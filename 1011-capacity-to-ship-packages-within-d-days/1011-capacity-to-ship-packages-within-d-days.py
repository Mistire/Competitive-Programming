class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def helper(mid):
            numSum = 0
            count = 1
            for weight in weights:
                if numSum + weight <= mid:
                    numSum += weight
                else:
                    count += 1
                    numSum = weight
            return count

        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left+right) // 2

            if helper(mid) > days:
                left = mid + 1
            else:
                right = mid - 1
        return left

