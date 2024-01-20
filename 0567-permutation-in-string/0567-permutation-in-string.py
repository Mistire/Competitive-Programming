class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1, lenS2 = len(s1), len(s2)
        if lenS1 > lenS2:
            return False
        counterS1 = Counter(s1)
        counterWindow = Counter(s2[:lenS1])
        
        for i in range(lenS2 - lenS1):
            if counterS1 == counterWindow:
                return True
            counterWindow[s2[i]] -= 1
            if counterWindow[s2[i]] == 0:
                del counterWindow[s2[i]]
            counterWindow[s2[i+lenS1]] += 1
        return counterS1 == counterWindow