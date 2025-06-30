import collections
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        l = 0
        nums.sort()
        print(nums)
        for r in range(len(nums)):
            while nums[r] - nums[l] > 1:
                l += 1
            if nums[r] - nums[l] == 1:
                res = max(res, r - l + 1)
        
        return res
    
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        res = 0
        for value in c:
            if (value + 1) in c:
                res = max(res, c[value] + c[value + 1])
        
        return res