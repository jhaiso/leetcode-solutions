from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr = []
        def backtrack(idx: int):
            if idx == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[idx])
            backtrack(idx + 1)
            curr.pop()
            backtrack(idx + 1)

        backtrack(0)
        return res
    
