class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        sumDict = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                sumDict[row+col].append(mat[row][col])
        
        for numSum, val in sumDict.items():
            if numSum % 2 == 0:
                res.extend(val[::-1])
            else:
                res.extend(val)
                    
        return res