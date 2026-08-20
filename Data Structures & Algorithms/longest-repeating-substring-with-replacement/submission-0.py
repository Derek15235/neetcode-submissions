class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        maxLen = 1
        for c in charSet:
            l = 0
            # Count the actual appearances of c
            count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                # While the number of replcaements is more than k, move left boundary forward
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                maxLen = max(r - l + 1, maxLen)
            
                

        
        return maxLen
        
