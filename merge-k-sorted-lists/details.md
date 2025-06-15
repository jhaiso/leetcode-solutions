# 23. Merge k Sorted Lists

## Relevant Topics

Linked List, Heap (Priority Queue)

## Solution Thought Process

### Brute Force

Keep a pointer for every list. At each step, find the node with the smallest value, and add it to the current list.
Time Complexity: O(n \* k)
Space Complexity: O(1) extra space

### Sorting

Sort all the nodes, and reassemble.
Time Complexity: O(nlogn)
Space Complexity: O(n)

### Heap (Priority Queue)

We see that at each step, we want the node that has the smallest value from all the lists. When continuously accessing a maximum/minimum value, a heap comes to mind. We keep pointers for each list. We add them all to a min heap. At each step, we pop, add to list, set the pointer to next, and push back onto the heap.

```python

```
Time Complexity: O(nlogk)
Space Complexity: O(k)

### Divide and Conquer

We can continuously merge lists in O(n) time. Since we merge two at a time and reduce the number of lists by a factor of 2, it runs in O(nlogk) time.