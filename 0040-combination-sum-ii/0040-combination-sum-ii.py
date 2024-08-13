class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backTrack(index, comb, target):
            if target == 0:
                res.append(comb[:])
                return
            if target < 0:
                return
            
            prev = -1

            for i in range(index, len(candidates)):
                if prev == candidates[i]:
                    continue
                comb.append(candidates[i])
                backTrack(i+1, comb, target-candidates[i])
                comb.pop()

                prev = candidates[i]

        backTrack(0, [], target)
        return res


