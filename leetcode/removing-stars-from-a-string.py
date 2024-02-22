class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if s[i] == "*":
                stack.pop()
                stack.pop()
        newStr = ''.join(stack)
        return newStr