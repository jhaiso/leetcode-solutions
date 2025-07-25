from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        permutations = self.permute(nums[1:])
        res = []
        for p in permutations:
            for i in range(0, len(p)+1):
                p_copy = p[:]
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res