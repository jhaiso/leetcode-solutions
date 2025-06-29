from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        num_oranges = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_oranges += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        def addCell(r, c):
            nonlocal num_oranges
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if grid[r][c] != 1:
                return
            # Now we know it's a fresh orange
            grid[r][c] = 2  # mark as rotten
            num_oranges -= 1
            q.append((r, c))

        dist = 0
        while q and num_oranges > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
            dist += 1

        return dist if num_oranges == 0 else -1
