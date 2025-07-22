from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # let's use a sliding window approach
        res = 0

        seen = set()
        curr = 0
        l = 0
        for r in range(len(nums)):
            while nums[r] in seen:
                curr -= nums[l]
                seen.remove(nums[l])
                l += 1

            seen.add(nums[r])
            curr += nums[r]
            res = max(res, curr)
        
        return res