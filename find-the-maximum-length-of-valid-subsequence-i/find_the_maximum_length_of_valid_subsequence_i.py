from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        evens, alternating = nums[0] % 2 == 0, 1
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                evens += 1
            if nums[i-1] % 2 != nums[i] % 2:
                alternating += 1
        
        return max(evens, len(nums) - evens, alternating)