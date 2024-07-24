class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)  
        sum = 0
        steps = 0
        
        while sum < target or (sum - target) % 2 != 0:
            steps += 1
            sum += steps
        
        return steps