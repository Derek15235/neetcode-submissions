class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        longest = 1
        l, r = 0, 1
        currSub = set()
        currSub.add(s[l])
        while r < len(s):
            while s[r] in currSub:
                currSub.remove(s[l])
                l += 1
            currSub.add(s[r])
            currLen = r - l + 1
            longest = max(currLen, longest)
            r += 1

        return longest