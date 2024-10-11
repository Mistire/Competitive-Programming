class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
         # Step 1: Initialize the distance array
        dist = [float('inf')] * n
        dist[src] = 0  # The cost to reach the source city is 0
        
        # A temporary distance array to store results for the current iteration
        temp_dist = dist[:]
        
        # Step 2: Perform K+1 relaxations (because K stops means K+1 edges)
        for i in range(k + 1):
            # Iterate over all the flights (edges)
            for u, v, w in flights:
                # If the source city has been reached
                if dist[u] != float('inf'):
                    # Relax the edge if a cheaper price is found
                    temp_dist[v] = min(temp_dist[v], dist[u] + w)
            
            # Update the main distance array with this iteration's results
            dist = temp_dist[:]
        
        # Step 3: Check if we found a valid path to the destination
        return dist[dst] if dist[dst] != float('inf') else -1