class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bestArea = -1

        l, r = 0, len(heights) - 1
        while l != r:
            currArea = (r - l) * min(heights[l], heights[r])
            bestArea = max(currArea, bestArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return bestArea
            
        