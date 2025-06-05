from typing import List


class Solution:
    def maxProfitTwoPointers(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            res = max(res, profit)
            if profit < 0:
                l = r
            r += 1
        
        return res
    
    def maxProfitDP(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0

        for sell in prices:
            res = max(res, sell - buy)
            buy = min(buy, sell)
        
        return res