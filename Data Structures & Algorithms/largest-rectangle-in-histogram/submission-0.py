class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (index, height)
        for i, h in enumerate(heights):
            curIndex = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                maxArea = max(maxArea, area)
                curIndex = index
            stack.append((curIndex, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea


