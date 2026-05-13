class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {
            "}" : "{",
            "]": "[",
            ")": "(" 
        }
        stack = []
        n = 0
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char in par_dict:
                if stack and stack[-1] == par_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        
        