class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1

        queue = deque()
        queue.append(["0000", 0])
        visit = set()
        visit.add(("0000"))

        while queue:
            key, move = queue.popleft()
            if key == target:
                return move
            for i in range(4):
                for j in [-1,0,1]:
                    ans = (int(key[i]) - j) % 10
                    new_key = key[:i] + str(ans) + key[i+1:]
                    if new_key not in visit and new_key not in deadends:
                        visit.add(new_key)
                        queue.append([new_key, move+1])
        return -1