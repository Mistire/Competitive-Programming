class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Step 2: Min-heap to store (price, city, stops)
        heap = [(0, src, 0)]  # (current cost, current city, number of stops)
        
        # Step 3: Distance table, but now we track the best cost with exact stops
        dist = {(src, 0): 0}  # (city, stops) => cost
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            
            # If we reach the destination, return the cost
            if node == dst:
                return cost
            
            # If we have reached the stop limit, skip this node
            if stops > k:
                continue
            
            # Process all the neighbors of the current node
            for neighbor, price in graph[node]:
                new_cost = cost + price
                if (neighbor, stops + 1) not in dist or new_cost < dist[(neighbor, stops + 1)]:
                    dist[(neighbor, stops + 1)] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor, stops + 1))
        
        return -1  # No valid path found