class Solution:
    def minScore(self, num_nodes: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
        
        min_score = float('inf')
        vis = set()
        queue = deque([1])

        while queue:
            node = queue.popleft()
            for adj, score in graph[node].items():
                if adj not in vis:
                    queue.append(adj)
                    vis.add(adj)
                min_score = min(min_score, score)
                
        return min_score