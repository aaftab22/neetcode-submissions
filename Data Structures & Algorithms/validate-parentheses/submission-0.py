class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '[' or i == '(' or i == '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                elif stack[-1] == "[" and i == "]":
                    stack.pop()
                elif stack[-1] == '{' and i == "}":
                    stack.pop()
                elif stack[-1] == "(" and i == ")" :
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True