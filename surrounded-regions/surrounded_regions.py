from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        seen = [[False] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == "X" or seen[r][c]:
                return
            seen[r][c] = True
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(1, ROWS-1):
            dfs(r, 0)
            dfs(r, COLS-1)
        
        for c in range(1, COLS-1):
            dfs(0, c)
            dfs(ROWS-1, c)
        
        print(seen)
        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                if not seen[r][c]:
                    board[r][c] = "X"