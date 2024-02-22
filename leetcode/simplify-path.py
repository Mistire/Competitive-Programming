class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathArr = path.split("/")

        for i in pathArr:
            if stack and i == "..":
                stack.pop()
            elif i not in ["", "..", "."]:
                stack.append(i)
        return "/" + "/".join(stack)

    