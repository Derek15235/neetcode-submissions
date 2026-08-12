class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_groups = defaultdict(list)
        for string in strs:
            counts = [0] * 26
            for c in string:
                counts[ord(c) - ord('a')] += 1
            str_groups[tuple(counts)].append(string)
           
        return list(str_groups.values())