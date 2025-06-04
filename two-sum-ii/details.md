# 167. Two Sum II - Input Array Is Sorted
## Relevant Topics
Array, Hash Table, Binary Search, Two Pointer

## Solution Thought Process
### Brute Force
Same as Two Sum

### Binary Search
Since the array is sorted, for each index, we could perform a binary search on the subsequent elements to find target-element.
Time Complexity: O(nlogn) - binary search time = O(logn)
Space Complexity: 1

### Hash Map - One Pass
Same as Two Sum

### Two Pointer
We make the observation that if we begin on the smallest and largest values of the array, there are three cases. (1) The value sum is the target, (2) the sum is less than the target (increment the smaller), or (3) the sum is greater than the target (decrement the larger).
Time Complexity: O(n)
Space Complexity: O(1)