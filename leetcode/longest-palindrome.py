class Solution:
    def longestPalindrome(self, s: str) -> int:
        countStr = Counter(s)
        sumCount = 0
        
        for i in countStr:
            sumCount += (countStr[i] // 2) * 2
            if sumCount % 2 == 0 and countStr[i] % 2 == 1:
                sumCount += 1
        return sumCount
