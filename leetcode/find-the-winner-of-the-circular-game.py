class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friend = [i + 1 for i in range(n)]
        cur = 0

        while len(friend) > 1:
            cur = ((cur + k ) - 1) % len(friend)
            friend.pop(cur)
        return friend[0]

                
        

