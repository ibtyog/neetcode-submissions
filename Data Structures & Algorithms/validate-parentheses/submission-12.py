class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {
            "}" : "{",
            "]": "[",
            ")": "(" 
        }
        closer = par_dict.keys()
        stack = []
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char not in closer:
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != par_dict[char]:
                    return False
                else:
                    stack.pop()
        return True and len(stack) == 0
        