from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        res = 0
        for p in [[0, 0], [1, 1], [0, 1], [1, 0]]:
            count = 0
            for n in nums:
                if n % 2 == p[count % 2]:
                    count += 1
            res = max(res, count)
        return res