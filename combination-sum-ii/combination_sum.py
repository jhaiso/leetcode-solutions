class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []
        def backtrack(idx, s):
            if s == target:
                res.append(curr[:])
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if s + candidates[i] > target:
                    return
                curr.append(candidates[i])
                backtrack(i+1, s+candidates[i])
                curr.pop()
        
        backtrack(0, 0)
        return res