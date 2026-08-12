class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        C = [0] * n
        if int(s[0]) > 0:
            C[0] = 1
        if n == 1:
            return C[0]
        if 10 <= int(s[:2]) <= 26:
            C[1] = 1
        
        if int(s[1]) > 0:
            C[1] += C[0]
        

        for i in range(2, n):
            if int(s[i]) > 0:
                C[i] += C[i - 1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                C[i] += C[i - 2]
    
        return C[n-1]