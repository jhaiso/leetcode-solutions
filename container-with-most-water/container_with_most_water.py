from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        most = 0

        l, r = 0, len(height) - 1
        while l < r:
            most = max(most, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return most