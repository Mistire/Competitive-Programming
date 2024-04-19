class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        arrTup = [(abs(a-x), a) for a in arr]
        arrSm = nsmallest(k, arrTup)
        res = [num for dif, num in arrSm]
        res.sort()
        return res