class Solution:
    def sortSentence(self, s: str) -> str:
        strs = s.split()
        strs.sort(key=lambda x:x[-1])
        return ' '.join(st[:-1] for st in strs)