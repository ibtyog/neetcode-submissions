class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {
            "}" : "{",
            "]": "[",
            ")": "(" 
        }
        closer = par_dict.keys()
        stack = []
        n = 0
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char not in closer:
                stack.append(char)
                n+=1
            else:
                if n == 0 or stack[-1] != par_dict[char]:
                    return False
                else:
                    stack.pop()
                    n-=1
        return True and n == 0
        