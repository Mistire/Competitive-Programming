class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # res2 = []
        # for i in range(len(matrix)):
        #     old = []
        #     for j in range(len(matrix[0])):
        #         old.append(matrix[i][j])
        #     res2.append(old)
            
        res = []
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            res.append(temp)
        return res