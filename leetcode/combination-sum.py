class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        total = 0
        candidates.sort()

        def backTrack(index, comb):
            nonlocal target, total
            
            if total == target:
                return res.append(comb[:])
            if target < candidates[index] or target < total:
                return

            for i in range(index, len(candidates)):
                comb.append(candidates[i])
                total += candidates[i]
                if total <= target:
                    backTrack(i, comb)
                total -= comb.pop()
        
        backTrack(0, [])
        return res










