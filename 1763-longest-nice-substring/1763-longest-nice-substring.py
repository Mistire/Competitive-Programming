class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isNice(sub):
            return all(c.swapcase() in sub for c in sub)
        maxLength = 0
        result = ""
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                currentSubstring = s[i:j]
                if isNice(currentSubstring) and len(currentSubstring) > maxLength:
                    maxLength = len(currentSubstring)
                    result = currentSubstring
        return result