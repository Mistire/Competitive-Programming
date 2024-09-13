class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefiXor = [0] * (len(arr)+1)
        res = []
        
        for i in range(1, len(arr)+1):
            prefiXor[i] = prefiXor[i-1] ^ arr[i-1]
        
        for left, right in queries:
            res.append(prefiXor[left] ^ prefiXor[right+1])
        return res
