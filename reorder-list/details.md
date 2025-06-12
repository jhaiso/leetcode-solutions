# 143. Reorder List
## Relevant Topics
Linked List, Two Pointer (Fast and Slow Pointers), Stack

## Solution Thought Process
### Reverse Second Half (Two Pointer)
Initially, I thought of splitting the linked list into two halves using a fast and slow pointer, reversing the second half, and merging the two.
Time Complexity: O(n)
Space Complexity: O(n)

### Optimization (Stack)
Rather than reversing the second half, we push all the values onto a stack. Then, we merge by popping.
Time Complexity: O(n)
Space Complexity: O(n)