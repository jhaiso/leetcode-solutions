from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or not grid[r][c]:
                return 0
            grid[r][c] = 0
            return (1 +
                    dfs(r+1, c) +
                    dfs(r-1, c) +
                    dfs(r, c+1) +
                    dfs(r, c-1))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    res = max(res, dfs(r, c))
        
        return res