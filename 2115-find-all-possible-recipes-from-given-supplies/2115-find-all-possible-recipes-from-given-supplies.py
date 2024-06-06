class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        rec_dict = defaultdict(list)
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for i in range(len(recipes)):
            rec_dict[recipes[i]] = ingredients[i]
            indegree[recipes[i]] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])

        queue = deque(supplies)
        supply_set = set(supplies)
        res = []

        while queue:
            item = queue.popleft()
            if item in rec_dict:
                res.append(item)

            for nei in graph[item]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return res