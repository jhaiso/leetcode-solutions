from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = len(fruits)
        for fruit in fruits:
            for i in range(len(baskets)):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    res -= 1
                    break
        
        return res