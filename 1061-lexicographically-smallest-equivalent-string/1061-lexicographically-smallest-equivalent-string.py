class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        for i in range(26):
            parent[chr(97 + i)] = chr(97 + i)
        # print(parent)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[parent[x]]
            return x

        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                if px < py:
                    parent[py] = px
                else:
                    parent[px] = py
        
        for i in range(len(s2)):
            union(s1[i], s2[i])

        res = []
        for i in range(len(baseStr)):
            res.append(find(baseStr[i]))
        return "".join(res)
        

        


