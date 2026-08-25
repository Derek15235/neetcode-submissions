class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterDict = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        res = []
        def dfs(start, path):
            if start == len(digits):
                if len(path) > 0:
                    res.append("".join(path))
                return
            
            for letter in letterDict[digits[start]]:
                path.append(letter)
                dfs(start+1, path)
                path.pop()
        dfs(0, [])
        return res

                