class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (j - i <= 2 or dp[i + 1][j - 1]) and s[i] == s[j]
                if dp[i][j]:
                    count += 1
        
        return count