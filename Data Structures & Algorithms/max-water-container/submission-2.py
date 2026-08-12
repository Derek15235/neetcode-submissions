class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bestVol = 0
        l, r = 0, len(heights) - 1

        while l < r:
            vol = min(heights[l], heights[r]) * (r - l)
            if vol > bestVol:
                bestVol = vol
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return bestVol