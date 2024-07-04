class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        
        for x, y in pairs:
            uf.union(x, y)
        
        root_to_indices = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            root_to_indices[root].append(i)
        
        smallest_string = list(s)
        for indices in root_to_indices.values():
            chars = [s[i] for i in indices]
            chars.sort()
            for i, char in zip(sorted(indices), chars):
                smallest_string[i] = char
        
        return ''.join(smallest_string)









