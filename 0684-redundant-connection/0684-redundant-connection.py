class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = [1] * (len(edges)+1)
        parent = {i:i for i in range(len(edges)+1)}

        def find(x):
            while x != parent[x]:
                x = parent[parent[x]]
            return x

        def union(x, y):
            p1 = find(x)
            p2 = find(y)

            if p1 == p2:
                return False

            if p1 != p2:
                if size[p1] > size[p2]:
                    parent[p2] = p1
                    size[p1] += size[p2]
                else:
                    parent[p1] = p2
                    size[p2] += size[p1]
            return True
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        
                
