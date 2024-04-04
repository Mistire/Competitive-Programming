class Solution:
    def findCircleNum(self, isc: List[List[int]]) -> int:
        graph = defaultdict(list)
        count = 0
        visited = set()

        for node1 in range(len(isc)):
            for node2 in range(len(isc)):
                if isc[node1][node2] == 1:
                    graph[node1].append(node2)
                    graph[node2].append(node1)
            
        def dfs(node):
            nonlocal count
            visited.add(node)

            for neighbours in graph[node]:
                if neighbours not in visited:
                    dfs(neighbours)
        
        for node in range(len(isc)):
            if node not in visited:
                dfs(node)
                count += 1
        
        return count

        
        
