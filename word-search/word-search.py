from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def backtrack(r, c, idx):
            if idx == len(word):
                return True
            if r<0 or c<0 or r >= ROWS or c >= COLS or word[idx] != board[r][c] or board[r][c] == '#':
                return False
            
            board[r][c] = '#'
            res = (backtrack(r + 1, c, idx + 1) or
                   backtrack(r - 1, c, idx + 1) or
                   backtrack(r, c + 1, idx + 1) or
                   backtrack(r, c - 1, idx + 1))
            board[r][c] = word[idx]
            return res
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        
        return False