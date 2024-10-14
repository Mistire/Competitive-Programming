class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist_arr = [float('inf')] * n
        dist_arr[src] = 0

        temp_arr = dist_arr[:]

        for i in range(k+1):
            for u, v, w in flights:
                if dist_arr[u] != float('inf'):
                    temp_arr[v] = min(temp_arr[v], dist_arr[u] + w)
            dist_arr = temp_arr[:]
        return dist_arr[dst] if dist_arr[dst] != float('inf') else -1