# 33. Search in Rotated Sorted Array
## Relevant Topics
Array, Binary Search

## Solution Thought Process
Given that the array is sorted, binary search comes to mind. How can we apply it?

We see that when we divide the array in the middle, there are two cases. Either the right half is sorted, or the left half is sorted. Then, we adjust the left and right pointers accordingly.

Time Complexity: O(logn)
Space Complexity: O(1)