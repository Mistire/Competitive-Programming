class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1, n+1)}
        dist_dict = {i:float('inf') for i in range(1, n+1)}
        dist_dict[k] = 0
        heap = [(0, k)]

        for u, v, w in times:
            graph[u].append((v, w))
        
        while heap:
            curr_dist, node = heapq.heappop(heap)

            for nei, wei in graph[node]:
                new_dist = curr_dist + wei
                if new_dist < dist_dict[nei]:
                    dist_dict[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))
        max_dist = max(dist_dict.values())
        return max_dist if max_dist < float('inf') else -1