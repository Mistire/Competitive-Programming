class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        total = 0
        comb = []
        ans = []
        candidates.sort()

        def backTrack(index):
            nonlocal total, target

            if total == target:
                ans.append(comb.copy())
                return
            if candidates[index] > target or total > target:
                return

            for i in range(index, len(candidates)):
                total += candidates[i]
                comb.append(candidates[i])
                if total <= target:
                    backTrack(i)
                total -= comb.pop()

        backTrack(0)
        return ans

