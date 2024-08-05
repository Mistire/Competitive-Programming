class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        strs_dict = {}

        for strs in arr:
            if strs in strs_dict:
                strs_dict[strs] += 1
            else:
                strs_dict[strs] = 1

        strs_arr = [strs for strs, cnt in strs_dict.items() if cnt == 1]
        
        if k <= len(strs_arr):
            return strs_arr[k-1]
        else:
            return ""
            