class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount = Counter(p)
        ans = []
        k = len(p)

        for i in range(len(s) - k + 1):
            window = s[i : i+k]
            wCount = Counter(window)
            if wCount == pCount:
                ans.append(i)
        return ans





