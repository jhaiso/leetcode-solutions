from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        res = 0

        def DFS(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or visited[r][c] or grid[r][c] == "0":
                return
            visited[r][c] = True
            DFS(r+1, c)
            DFS(r-1, c)
            DFS(r, c+1)
            DFS(r, c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if not visited[r][c] and grid[r][c] == "1":
                    DFS(r, c)
                    res += 1
        return res