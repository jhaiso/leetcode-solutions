# 4. Median of Two Sorted Arrays
## Relevant Topics
Array, Binary Search

## Solution Thought Process
### Brute Force
The brute force solution involves merging the two arrays, and finding the median.

Time Complexity: O(n+m)
Space Complexity: O(n+m)

### Binary Search
We see that in finding the median, we are dividing the array into two halves. We must ensure a few conditions: 1. the sum of the left sides of the arrays must be equal to half of the total. 2. In the division of each array, the largest value of the left side of array A must be <= the smallest value of the right side of array B and vice versa.
