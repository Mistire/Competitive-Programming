class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1]* len(graph)
        
        # def dfs(node):
        #     for neighbours in graph[node]:
        #         if color[neighbours] == -1:
        #             if color[node] == 0:
        #                 color[neighbours] = 1
        #             else:
        #                 color[neighbours] = 0
        #             if not dfs(neighbours):
        #                 return False
        #         else:
        #             if color[node] == color[neighbours]:
        #                 return False
        #     return True

        # for node in range(len(graph)):
        #     if color[node] == -1:
        #         color[node] = 0
        #         if not dfs(node):
        #             return False
        # return True

        for node in range(len(graph)):
            if color[node] == -1:
                stack = [node]
                color[node] = 0

            while stack:
                node = stack.pop()

                for neighbours in graph[node]:
                    if color[neighbours] == -1:
                        color[neighbours] = abs(color[node] - 1)
                        stack.append(neighbours)
                    elif color[node] == color[neighbours]:
                        return False
        return True

            























