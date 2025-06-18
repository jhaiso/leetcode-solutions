# 2966. Divide Array Into Arrays With Max Difference
## Relevant Topics
Array, Sorting, Hash Table, Greedy

## Solution Thought Process
### Brute Force
Check every possible division of arrays into arrays of size 3, check if the array satisfies the conditions.
Time Complexity: O(n^3)
Space Complexity: O(1)

### Sorting / Greedy
We simply sort the array, and divide the array into subarrays rather than finding the permutations.
Time Complexity: O(nlogn)
Space Complexity: O(n)
