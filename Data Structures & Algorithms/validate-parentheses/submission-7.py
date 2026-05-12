class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        parenth = {
            ")":"(",
            "]":"[",
            "}":"{",
        }
        stack = []
        for char in s:
            if char not in parenth:
                stack.append(char)
            else:
                if len(stack) != 0:
                    if parenth[char] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        return False