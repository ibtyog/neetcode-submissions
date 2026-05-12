class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s += word + '\n'
        return s
    def decode(self, s: str) -> List[str]:
        return s.split('\n')[:-1]