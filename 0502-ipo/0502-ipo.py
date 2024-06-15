class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        project = sorted(zip(capital, profits))
        max_heap = []
        index = 0
        
        for _ in range(k):
            while index < len(project) and project[index][0] <= w:
                heappush(max_heap, -project[index][1])
                index += 1
            
            if not max_heap:
                break
            
            w -= heappop(max_heap)
        
        return w