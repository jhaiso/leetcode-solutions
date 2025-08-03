from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left, right = 0, 0
        n = len(fruits)
        total = 0
        res = 0

        def step(left, right):
            if fruits[right][0] <= startPos:
                return startPos - fruits[left][0]
            elif fruits[left][0] >= startPos:
                return fruits[right][0] - startPos
            else:
                return (
                    min(
                        fruits[right][0] - startPos,
                        startPos - fruits[left][0],
                    )
                    + fruits[right][0]
                    - fruits[left][0]
                )
        
        while right < n:
            total += fruits[right][1]
            while left <= right and step(left, right) > k:
                total -= fruits[left][1]
                left += 1
            
            res = max(res, total)
            right += 1

        return res
