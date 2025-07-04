import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if q[0] < l:
                q.popleft()
            if r >= k-1:
                res.append(nums[q[0]])
                l += 1
            r += 1
    
        return res
