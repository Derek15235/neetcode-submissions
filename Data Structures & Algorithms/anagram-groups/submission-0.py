class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Keys: Character Maps
        # Values: List on the strings who have that character map
        c_maps = defaultdict(list)

        # Iterate through each string, get character map, find a match or make new list for that map
        for s in strs:
            c_map = [0] * 26
            for c in s:
                c_map[ord(c) - ord('a')] += 1

            c_maps[tuple(c_map)].append(s)

        return list(c_maps.values())