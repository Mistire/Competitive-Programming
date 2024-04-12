class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        seen = [False] * len(rooms)
        seen[0] = True

        while queue:
            node = queue.popleft()
            for key in rooms[node]:
                if not seen[key]:
                    seen[key] = True
                    queue.append(key)
        return all(seen)


        
            


