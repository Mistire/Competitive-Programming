class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        numDict = {}

        for i, x in enumerate(arr2):
            numDict[x] = i

        arr1.sort(key=lambda x: numDict.get(x, 10000+x))
        return arr1