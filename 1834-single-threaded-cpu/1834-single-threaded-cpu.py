class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key=lambda x:x[0])
        
        heap, res = [], []
        time, i = tasks[0][0], 0
        

        while heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if not heap:
                time = tasks[i][0]

            else:
                proT, idx = heappop(heap)
                time += proT
                res.append(idx)
        return res

