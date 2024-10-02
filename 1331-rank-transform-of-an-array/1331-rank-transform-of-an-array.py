class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        res = []
        set_arr = set(arr)
        sort_arr = sorted(list(set_arr))
        dict_arr = {num:i for i, num in enumerate(sort_arr)}

        for i in range(len(arr)):
            if arr[i] in dict_arr:
                res.append(dict_arr[arr[i]]+1)
        return res

        