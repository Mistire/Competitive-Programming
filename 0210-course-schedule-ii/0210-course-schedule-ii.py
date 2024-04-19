class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        queue = deque()

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
        
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in graph[node]:
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    queue.append(nei) 

        return res if numCourses == len(res) else []