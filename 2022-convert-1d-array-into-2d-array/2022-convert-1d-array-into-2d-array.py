class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n * m:
            return []

        res = []
        temp = []
        count = 0

        for val in original:
            temp.append(val)
            count += 1

            if count == n:
                res.append(temp)
                temp = []
                count = 0
        return res