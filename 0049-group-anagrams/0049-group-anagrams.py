class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            strs_dict[sorted_s].append(s)
        return strs_dict.values()