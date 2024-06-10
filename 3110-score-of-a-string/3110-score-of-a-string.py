class Solution:
    def scoreOfString(self, s: str) -> int:
        arr = [ord(i) for i in s]
        tot = 0
        
        for i in range(1, len(arr)):
            tot += abs(arr[i-1] - arr[i])
        return tot
