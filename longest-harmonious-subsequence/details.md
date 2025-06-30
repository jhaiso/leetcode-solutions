# 594. Longest Harmonious Subsequence

## Relevant Topics

Sorting, Two Pointers, Hash Table

## Solution Thought Process
### Brute Force
The brute force solution involves finding all possible subsequences, finding the maximum and minimum, and returning the length of the longest one. 
Time Complexity: O(2^n) - include/exclude elements
Space Complexity: O(n)

### Sorting | Two Pointers
We first sort the array. Although the order of elements does change, for each contiguous subarray in the sorted array, there exists a subarray in the original. We maintain two pointers, one for the maximum value of the subarray and one for the minimum. We maintain the condition that the maximum differences is exactly 1.
Time Complexity: O(nlogn)
Space Complexity: O(n)

### Hash Table
We create a hash table to keep track of the count of each of the values. Then for each value, if the value + 1 is in the hashtable, we compare the sum of the two counts to the result.
Time Complexity: O(n)
Space Complexity: O(n)