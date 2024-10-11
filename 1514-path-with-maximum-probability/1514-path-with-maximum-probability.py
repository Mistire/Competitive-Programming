class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        prob_dict = {i:0 for i in range(n)}
        prob_dict[start_node] = 1
        heap = [(1, start_node)]

        for i, (u, v) in enumerate(edges):
            graph[u].append((v,i))
            graph[v].append((u,i))
        
        while heap:
            curr_prob, curr_node = heapq.heappop(heap)
         
            for nei, edg_idx in graph[curr_node]:
                new_prob = curr_prob * succProb[edg_idx]
                if new_prob < 1e-5:
                    new_prob = 0
                if new_prob > prob_dict[nei]:
                    prob_dict[nei] = new_prob
                    heapq.heappush(heap, (new_prob, nei))
        return float(prob_dict[end_node]) if prob_dict[end_node] > 0 else float(0)