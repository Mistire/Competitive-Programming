class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preq = [[] * numCourses for _ in range(numCourses)]
        for pre, course in prerequisites:
            preq[pre].append(course)

        reach = [[False] * numCourses for _ in range(numCourses)]
        res = []

        for i in range(numCourses):
            queue = deque([i])
            visit = set([i])

            while queue:
                node = queue.popleft()
                
                for nei in preq[node]:
                    if nei not in visit:
                        visit.add(nei)
                        queue.append(nei)
                        reach[node][nei] = True
        res = []
        for u, v in queries:
            res.append(reach[u][v])

        return res

        

        

        
        