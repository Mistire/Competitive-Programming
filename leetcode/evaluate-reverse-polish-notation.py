class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["*","/","-","+"]:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == "*":
                    result = num1 * num2
                elif i == "-":
                    result = num1 - num2
                elif i == "/" and num2 != 0:
                    result = int(num1 / num2)
                elif i == "+":
                    result = num1 + num2
                stack.append(str(result))
            else:
                stack.append(i)
                
        return int(stack[-1])
                    

                
                