class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ans = {i for i in range(n)}
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
        for value in graph.values():
            for x in value:
                if x in ans:
                    ans.discard(x)
        if len(ans) == 1:
            for num in ans:
                return num
        else:
            return -1
        