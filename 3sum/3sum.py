from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, v in enumerate(nums):
            if v > 0:                     # if the first value is positve, all others must also be positive and sum > 0
                break                     # so we can break
            if i > 0 and v == nums[i-1]:  # skipping duplicates
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = nums[l] + nums[r]
                if v + curr < 0:
                    l += 1
                elif v + curr > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r: # only if a solution is found do we need to consider skipping
                        l += 1
        
        return res