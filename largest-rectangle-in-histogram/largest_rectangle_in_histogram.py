from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] >= h:
                height, index = stack.pop()
                start = index
                largest = max(largest, (i - index) * height)
            stack.append((h, start))
        
        for h, i in stack:
            largest = max(largest, (len(heights) - i) * h)
        
        return largest