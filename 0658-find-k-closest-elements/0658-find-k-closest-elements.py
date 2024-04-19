class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heapify(arr)
        numS = nsmallest(k, arr)
        return numS