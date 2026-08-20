class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                idx = stack.pop()
                height = heights[idx]
                right = i - 1
                left = stack[-1] + 1 if stack else 0
                width = right - left + 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea