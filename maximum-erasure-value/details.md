# 1695. Maximum Erasure Value
## Topics
Sliding window

## Solution Thought Process
Because we are working with contiguous subsequences given a certain condition, sliding window comes to mind. Specifically, we keep track of the current sum of the elements in the window, and the current elements present. We iterate the right pointer until we find a duplicate, and then increment the left pointer until that duplicate value is no longer in the array.

Time Complexity: O(n) - 2 iterations through the array
Space Complexity: O(n) - set