class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0

        while target > startValue:
            count += 1
            if target % 2 != 0:
                target += 1
            else:
                target //= 2
        return count + startValue - target