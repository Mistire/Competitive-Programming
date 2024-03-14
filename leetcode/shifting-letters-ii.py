class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        res = [0] * (len(s)+1)

        for i in range(len(shifts)):
            if shifts[i][2] == 0:
                res[shifts[i][0]] -= 1
                res[shifts[i][1]+1] += 1
            else:
                res[shifts[i][0]] += 1
                res[shifts[i][1]+1] -= 1

        ans = []
        preSum = 0
        for i in range(len(s)):
            preSum += res[i]
            ans.append(chr((((ord(s[i]) + preSum) - 97) % 26) + 97))

        return "".join(ans)


                
                


