class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        import math

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        lcm = divisor1 * divisor2 // gcd(divisor1, divisor2)
        
        left, right = 1, 2 * (uniqueCnt1 + uniqueCnt2)
        
        while left < right:
            mid = (left + right) // 2
            
            # Count of numbers not divisible by divisor1 up to mid
            count1 = mid - mid // divisor1
            # Count of numbers not divisible by divisor2 up to mid
            count2 = mid - mid // divisor2
            # Count of numbers not divisible by either divisor1 or divisor2 up to mid
            count_common = mid - mid // lcm
            
            # Check if it's possible to form the sets
            if count1 >= uniqueCnt1 and count2 >= uniqueCnt2 and count_common >= (uniqueCnt1 + uniqueCnt2):
                right = mid
            else:
                left = mid + 1
        
        return left
