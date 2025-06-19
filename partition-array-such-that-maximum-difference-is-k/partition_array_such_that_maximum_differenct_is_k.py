from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        start = float('-inf')

        for n in nums:
            if n - start > k:
                res += 1
                start = n
        
        return res