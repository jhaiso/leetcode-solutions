# 153. Find Minimum in Rotated Sorted Array
## Relevant Topics
Array, Binary Search

## Solution Thought Process
### Binary Search
Because the array is sorted, we think of binary search, but how can we apply it if the array is rotated? We see that if the middle value is greater than the right, then the start of the array must be in the right half, and otherwise it's in the left half.

Time Complexity: O(logn)
Space Copmlexity: O(1)