class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        
        for s in strs:
            sorted_str = ''.join(sorted(s))
            str_dict[sorted_str].append(s)
        return str_dict.values()
