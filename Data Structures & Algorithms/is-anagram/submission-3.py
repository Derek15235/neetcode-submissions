class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create counts of letters for s
        s_counts = {}
        for c in s:
            if c not in s_counts:
                s_counts[c] = 1
            else:
                s_counts[c] += 1
        # Create counts of letters for t
        t_counts = {}
        for c in t:
            if c not in t_counts:
                t_counts[c] = 1
            else:
                t_counts[c] += 1
        return s_counts == t_counts