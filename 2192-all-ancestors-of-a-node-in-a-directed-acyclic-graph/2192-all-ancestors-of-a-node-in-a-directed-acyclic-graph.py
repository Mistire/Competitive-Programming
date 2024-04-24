class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        res = []
        ans = []
        q = deque()
        parDict =defaultdict(set)

        for p, c in edges:
            graph[p].append(c)
            indegree[c] += 1
        # print(graph)

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        
        while q:
            node = q.popleft()
            for nei in graph[node]:
                indegree[nei] -= 1
                parDict[nei].update(parDict[node]) 
                parDict[nei].add(node)
    
                if indegree[nei] == 0:
                    q.append(nei)
        for i in range(n):
            res.append(sorted(list(parDict[i])))
        
        return res
        