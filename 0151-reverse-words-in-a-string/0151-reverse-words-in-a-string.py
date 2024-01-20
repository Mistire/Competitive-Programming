class Solution:
    def reverseWords(self, s: str) -> str:
        stringBuild = collections.deque()
        start = -1
        
        i = 0
        while i < len(s):
            if s[i] != " ":
                start = i
                while i < len(s) and s[i] != " ":
                    i += 1
                stringBuild.appendleft(s[start:i])
                i -= 1
            i += 1
        return " ".join(stringBuild)