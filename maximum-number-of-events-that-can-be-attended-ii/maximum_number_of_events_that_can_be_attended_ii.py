from bisect import bisect_right
from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        dp = [[0] * (n+1) for _ in range(k+1)]
        starts = [start for start, e, v in events]

        for curr in range(n-1, -1, -1):
            for count in range(1, k+1):
                next_ind = bisect_right(starts, events[curr][1])
                dp[count][curr] = max(dp[count][curr+1], events[curr][2] + dp[count-1][next_ind])
        
        return dp[k][0]