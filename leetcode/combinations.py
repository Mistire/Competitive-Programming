class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backTrack(start, comb):
            if len(comb) == k:
                return res.append(comb[:])

            for i in range(start, n+1):
                comb.append(i)
                backTrack(i+1, comb)
                comb.pop()

        backTrack(1, [])
        return res