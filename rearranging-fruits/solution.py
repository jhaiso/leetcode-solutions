import collections
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c = collections.Counter(basket1)
        for b in basket2:
            c[b] -= 1
        
        needs_swapped = []
        for fruit, count in c.items():
            if count % 2 != 0:
                return -1
            needs_swapped += [fruit] * abs(count // 2)
        
        m = min(basket1 + basket2)
        needs_swapped.sort()
        return sum(min(2 * m, x) for x in needs_swapped[:len(needs_swapped)//2])