from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matches.sort(key = lambda x: x)
        loss = defaultdict(int)
        win = defaultdict(int)
        lossArr = []
        winArr = []
        ans = []

        for i in matches:
            w, l = i
            win[w] += 1
            loss[l] += 1
        
        for key in win:
            if key not in loss:
                winArr.append(key)
        winArr.sort()
        ans.append(winArr)

        # print(ans)

        for key, value in loss.items():
            if value == 1:
                lossArr.append(key)
        lossArr.sort()
        ans.append(lossArr)
        return ans
            

        

            