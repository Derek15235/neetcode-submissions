class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Counts = [0] * 26
        for c in s1:
            s1Counts[ord(c) - ord('a')] += 1
        
        # Fixed window size
        windowCounts = [0] * 26
        # First window
        l = 0
        for i in range(len(s1)):
            windowCounts[ord(s2[i]) - ord('a')] += 1
        if s1Counts == windowCounts:
            return True
        # Iterate
        for r in range(len(s1), len(s2)):
            windowCounts[ord(s2[l]) - ord('a')] -= 1
            windowCounts[ord(s2[r]) - ord('a')] += 1
            if s1Counts == windowCounts:
                return True
            l += 1
        return False


        
