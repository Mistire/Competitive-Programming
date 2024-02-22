class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # closeToOpen = {")":"(", "]":"[", "}":"{"}
        
        # for c in s:
        #     if c in closeToOpen:
        #         if stack and stack[-1] == closeToOpen[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        # return True if not stack else False
        dict_ = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in dict_:
                stack.append(i)
            else:
                if not stack or dict_[stack.pop()] != i:
                    return False
        return not stack
    
            












