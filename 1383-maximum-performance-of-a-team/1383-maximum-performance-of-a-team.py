class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True)
        
        max_performance = 0
        speed_sum = 0
        min_heap = []
        
        for eff, spd in engineers:
            heapq.heappush(min_heap, spd)
            speed_sum += spd
            
            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)
            
            performance = speed_sum * eff
            max_performance = max(max_performance, performance)
        
        return max_performance % (10**9 + 7)