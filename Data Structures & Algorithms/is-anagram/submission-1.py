class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s_map = {}
        for c in s:
            if c not in char_s_map:
                char_s_map[c] = 1
            else:
                char_s_map[c] += 1
        
        char_t_map = {}
        for c in t:
            if c not in char_t_map:
                char_t_map[c] = 1
            else:
                char_t_map[c] += 1
        
        return char_t_map == char_s_map
        
        