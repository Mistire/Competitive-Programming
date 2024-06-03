class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for src, dest in redEdges:
            red[src].append(dest)
        for src, dest in blueEdges:
            blue[src].append(dest)


        ans = [-1 for _ in range(n)]
        queue = deque()
        queue.append([0, 0, None])
        visit = set()
        visit.add((0,None))

        while queue:
            node, length, ed_col = queue.popleft()
            if ans[node] == -1:
                ans[node] = length

            if ed_col != "R":
                for nei in red[node]:
                    if (nei, "R") not in visit:
                        visit.add((nei, "R"))
                        queue.append([nei, length+1, "R"])
            if ed_col != "B":
                for nei in blue[node]:
                    if (nei, "B") not in visit:
                        visit.add((nei, "B"))
                        queue.append([nei, length+1, "B"])

        return ans




        