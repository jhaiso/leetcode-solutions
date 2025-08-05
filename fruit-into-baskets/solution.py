import collections
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        count = collections.defaultdict(int)
        types = 0
        l = 0
        for r in range(len(fruits)):
            if count[fruits[r]] == 0:
                types += 1
            count[fruits[r]] += 1
            while types > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    types -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res