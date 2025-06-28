import heapq
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i, n in enumerate(nums):
            heapq.heappush(heap, (-n, i))
        
        include = set()
        while len(include) < k:
            val, idx = heapq.heappop(heap)
            include.add(idx)
        
        res = []
        for i in range(len(nums)):
            if i in include:
                res.append(nums[i])
        
        return res
    
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        vals = [[i, nums[i]] for i in range(n)]  # auxiliary array
        # sort by numerical value in descending order
        vals.sort(key=lambda x: -x[1])
        # select the first k elements and sort them in ascending order by index
        vals = sorted(vals[:k])
        res = [val for idx, val in vals]  # target subsequence
        return res