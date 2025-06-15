from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r

        while l <= r:
            k = l + (r-l) // 2

            time = 0
            for p in piles:
                time += -(-p // k) # because p and k are always positive, this acts as a ceil function
            
            if time <= h:
                r = k - 1
                result = k
            else:
                l = k + 1
        
        return result