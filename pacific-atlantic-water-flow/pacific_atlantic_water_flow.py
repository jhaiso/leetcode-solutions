from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl = [[False] * COLS for _ in range(ROWS)]
        pac = [[False] * COLS for _ in range(ROWS)]

        def dfs(r, c, found, prev):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or prev > heights[r][c] or found[r][c]:
                return
            found[r][c] = True
            dfs(r+1, c, found, heights[r][c])
            dfs(r-1, c, found, heights[r][c])
            dfs(r, c+1, found, heights[r][c])
            dfs(r, c-1, found, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS-1])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if atl[r][c] and pac[r][c]:
                    res.append([r, c])
        
        return res