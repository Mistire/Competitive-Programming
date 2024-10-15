class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_dict = {")":"(", "]":"[", "}":"{"}

        for i in range(len(s)):
            if s[i] in p_dict.values():
                stack.append(s[i])
            elif s[i] in p_dict.keys():
                if stack and stack[-1] == p_dict[s[i]]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False