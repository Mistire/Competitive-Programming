class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_s = s1.split()
        s2_s = s2.split()
        strs_count = Counter(s1_s + s2_s)

        return [strs for strs in strs_count if strs_count[strs] == 1]


                
        