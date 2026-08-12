class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        currSub = set()
        for r in range(len(s)):
            while s[r] in currSub:
                currSub.remove(s[l])
                l += 1
            currSub.add(s[r])
            currLen = r - l + 1
            longest = max(currLen, longest)
        return longest