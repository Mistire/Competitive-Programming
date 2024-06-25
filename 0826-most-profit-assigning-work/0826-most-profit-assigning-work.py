class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))  
        total_profit = 0
        max_profit = 0
        worker.sort()  
        j = 0
        
        for skill in worker:
            while j < len(jobs) and jobs[j][0] <= skill:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            total_profit += max_profit
        
        return total_profit