class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        last_opened = []
        for char in s:
            if char == "[" or char == "(" or char == "{":
                last_opened.append(char)
            elif (char == "}" or char == "]" or char == ")") and len(last_opened) == 0:
                return False
            elif (char == "]" and last_opened[-1] != "["):
                return False
            elif char == ")" and last_opened[-1] != "(":
                return False
            elif char == "}" and last_opened[-1] !="{":
                return False
            else:
                last_opened.pop()
        if len(last_opened) == 0:
            return True
        return False