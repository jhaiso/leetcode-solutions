from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        
        return res
    
class OptimizedSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(1, n):
            prefix *= nums[i-1]
            res[i] *= prefix

        suffix = 1
        for i in range(n - 2, -1, -1):
            suffix *= nums[i+1]
            res[i] *= suffix

        return res