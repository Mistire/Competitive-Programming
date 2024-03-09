class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            strs = "".join(sorted(str(num)))
            if strs[0] == "0":
                for i in range(len(strs)):
                    if strs[i] != "0":
                        return int(strs[i] + strs[:i] + strs[i+1:])
            return int(strs)
        elif num == 0:
            return 0
        else:
            strs = "".join(sorted(str(num)[1:], reverse=True))
            return -int(strs)

            