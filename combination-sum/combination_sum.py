from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        curr = []
        def backtrack(idx: int, s: int):
            if s == target:
                res.append(curr[:])
                return
            if idx >= len(candidates) or s > target:
                return
            curr.append(candidates[idx])
            backtrack(idx, s+candidates[idx])
            curr.pop()
            backtrack(idx+1, s)
        
        backtrack(0, 0)
        return res

class Solution_Optimized:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        curr = []
        def backtrack(idx: int, s: int):
            if s == target:
                res.append(curr[:])
                return
            
            for i in range(idx, len(candidates)):
                if s + candidates[i] > target:
                    return
                curr.append(candidates[i])
                backtrack(i, s+candidates[i])
                curr.pop()
        
        backtrack(0, 0)
        return res