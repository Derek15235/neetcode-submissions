class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(word):
            return word == word[::-1]
        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return

            # Check if each substring from this starting point is a palindrome
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if isPalindrome(word):
                    path.append(word)
                    dfs(end, path)
                    path.pop()
        
        dfs(0,[])
        return res
        