# 1498. Number of Subsequences That Satisfy the Given Sum Condition

## Relevatn Topics

Sorting, Two Pointers, Binary Search

## Solution Thought Process

### Brute Force

The brute force solution involves checking all the subsequences, finding the minimum and maximum, and checking if the conditions are met.

Time Complexity: O(2^n) - finding all subsequences
Space Complexity: O(2^n) - resulting array

### Sorting, Two Pointers

We start by sorting the array. We notice that if a pair of numbers sums to less than the target, than all subsequences with the values as the max and min are included in the result. We initialize the left pointer as 0 and the right pointer as the final index of the array. If the sum of the elements at the left and right index are less than the target, than we increment the result by 2^(r-l) (all subsequences). Then, we increment l. Otherwise we decrement r.

```python
# initialize reuslt
# initalize left to 0 and right to len(nums) - 1
# while l <= r
#   if the sum of the values at l and r <= target
#     increment res by 2^(r-l)
#     increment left
#   otherwise
#     decrement right
```