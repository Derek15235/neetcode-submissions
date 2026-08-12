class Solution:

    def encode(self, strs: List[str]) -> str:
        full = ""
        for s in strs:
            length = len(s)
            full += str(length) + "#"
            for c in s:
                full += c
        return full

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            currLength = ''
            while s[i] != '#':
                currLength += s[i]
                i += 1
            i += 1
            currString = ''
            while len(currString) != int(currLength):
                currString += s[i]
                i += 1
            res.append(currString)
        return res
