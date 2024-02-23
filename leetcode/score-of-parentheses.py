class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    score = 0
                    while stack[-1] != '(':
                        score += stack.pop()
                    stack.pop()
                    stack.append(score * 2)
        return sum(stack)