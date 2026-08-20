from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        tCounts = Counter(t)
        windowCounts = Counter()
        
        required = len(tCounts)  # number of unique chars we need
        formed = 0               # how many unique chars are satisfied
        
        l = 0
        res_len = float('inf')
        res_start = 0
        
        for r in range(len(s)):
            c = s[r]
            windowCounts[c] += 1
            
            # If this char's count in window just matched t's requirement
            if c in tCounts and windowCounts[c] == tCounts[c]:
                formed += 1
            
            # Try to shrink from the left while all chars are satisfied
            while formed == required:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res_start = l
                
                left_c = s[l]
                windowCounts[left_c] -= 1
                if left_c in tCounts and windowCounts[left_c] < tCounts[left_c]:
                    formed -= 1
                l += 1
        
        return s[res_start:res_start + res_len] if res_len != float('inf') else ""