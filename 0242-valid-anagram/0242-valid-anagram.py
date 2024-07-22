class Solution:
    def isAnagram(self, st: str, te: str) -> bool:
        return Counter(st) == Counter(te)
        