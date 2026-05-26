class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_l, t_l = len(s), len(t)
        if s_l != t_l:
            return False
        
        s_dict, t_dict = {}, {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1

        return s_dict == t_dict