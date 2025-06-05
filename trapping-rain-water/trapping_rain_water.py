from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]

        while l < r:
            if lmax < rmax:
                total += lmax - height[l]
                l += 1
                lmax = max(lmax, height[l])
            else:
                total += rmax - height[r]
                r -= 1
                rmax = max(rmax, height[r])
        
        return total