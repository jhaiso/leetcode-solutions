# 74. Search a 2D Matrix
## Relevant Topics
Array, Binary Search, Matrix

## Solution Thought Process
### Binary Search
Because the elements in each row are in ascending order, and the first value of each row is larger than the last value of the previous row, we can linearize the matrix into an array, and conduct a binary search!