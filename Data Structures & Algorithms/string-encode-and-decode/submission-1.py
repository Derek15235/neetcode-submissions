class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < (len(s)):
            str_length = ""
            while s[i] != "#":
                str_length += s[i]
                i += 1
            # i is at index of #
            print(str_length)
            print(i)
            str_length = int(str_length)
            if str_length == 0:
                res.append("")
            else:
                res.append(s[i+1: i + (str_length + 1)])
            i += str_length + 1
        return res
