import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if int(board[i][j]) in rows[i]:
                    return False
                elif int(board[i][j]) in cols[j]:
                    return False
                elif int(board[i][j]) in grid[(i//3)*3 + (j//3)]:
                    return False
                else:
                    rows[i].add(int(board[i][j]))
                    cols[j].add(int(board[i][j]))
                    grid[(i // 3) * 3 + (j // 3)].add(int(board[i][j]))
        
        return True
    
class BitmaskSolution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        grids = [0] * 9

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                n = int(board[row][col])
                if (1 << n) & rows[row]:
                    return False
                if (1 << n) & cols[col]:
                    return False
                if (1 << n) & grids[(row // 3) * 3 + (col // 3)]:
                    return False
                rows[row] |= (1 << n)
                cols[col] |= (1 << n)
                grids[(row // 3) * 3 + (col // 3)] |= (1 << n)
        
        return True
                