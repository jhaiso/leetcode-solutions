# 704. Binary Search
## Relevant Topics
Binary Search, Recursion

## Solution Thought Process
### Binary Search
There are 2 ways of approaching a binary search problem: Recursion, Iteration

#### Recursion
When the left bound of the search area is greater than the right, we return -1 (since the value isn't present). Otherwise, we divide the space into 2. If the middle is the target, we return the index. Otherwise, we recursively search the appropraite half.


#### Iteration
While the left pointer is less than or equal to the right pointer, if the middle value is the value, we return that index. Otherwise we move the left or right pointer accordingly.