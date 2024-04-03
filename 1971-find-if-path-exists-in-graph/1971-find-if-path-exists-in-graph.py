class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # adjList = defaultdict(list)
        
        # for node1, node2 in edges:
        #     adjList[node1].append(node2)
        #     adjList[node2].append(node1)
            
        # visited = set()
        
        # def dfs(node):
        #     if node == destination:
        #         return True
        #     if node not in visited:
        #         visited.add(node)
                
        #         for neighbour in adjList[node]:
        #             result = dfs(neighbour)
        #             if result:
        #                 return True
                
        #         # Add this return statement for the case when destination is not reached
        #         return False
                    
        # return dfs(source)
        def dfs(node, visisted):
            if node == destination:
                return True
            visited.add(node)
            for neighbours in graph[node]:
                if neighbours not in visited:
                    found = dfs(neighbours, visited)
                    if found:
                        return True
            return False

        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()
        return dfs(source, visited)


























