class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot = sum(chalk)
        if k % tot == 0:
            return 0
        else:
            rem = k % tot
            for num in chalk:
                if rem > 0:
                    rem -= num
                else:
                    return num