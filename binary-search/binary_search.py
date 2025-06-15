from typing import List


class Solution_Recursive:
    def search(self, nums: List[int], target: int) -> int:
        return self.bs(0, len(nums)-1, nums, target)
    
    def bs(self, l, r, nums, target):
        if l > r:
            return -1
        
        m = l + ((r - l)) // 2
        if nums[m] > target:
            return self.bs(l, m-1, nums, target)
        elif nums[m] < target:
            return self.bs(m+1, r, nums, target)
        else:
            return m

class Solution_Iterative:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = l + ((r-l) // 2)

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        return -1