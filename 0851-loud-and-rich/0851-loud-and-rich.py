class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        res = [None for _ in range(len(quiet))]
        graph = defaultdict(list)
        for rich, poor in richer:
            graph[poor].append(rich)
        # print(graph)
        # return 1

        def dfs(node):
            minQ = node
            for nbr in graph[node]:
                if res[nbr] is None:
                    dfs(nbr)
                minQ = min(minQ, res[nbr], key=lambda x:quiet[x])
            res[node] = minQ

        for person in range(len(quiet)):
            if res[person] is None:
                dfs(person)
        return res

            
