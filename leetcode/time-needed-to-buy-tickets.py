class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque([(i,t) for i,t in enumerate(tickets)])
        time = 0

        while q:
            idx, val = q.popleft()
            val -= 1
            time += 1
            if val == 0:
                if idx == k:
                    return time
            else:
                q.append((idx, val))

            
            