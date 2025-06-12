# 141. Linked List Cycle
## Relevant Topics
Linked List, Hash Set, Two Pointers

## Solution Thought Process
### Hash Set
To keep track of duplicates, a hash set is always a good idea. We iterate throught the linked list, and if we arrive at a node we've seen before, then there is a cycle.
Time Complexity: O(n)
Space Complexity: O(n)

### Two Pointers (Fast and Slow Pointer)
We keep a fast and slow pointer. Each time we increment the slow pointer, we increment the fast pointer twice. If there is as cycle, the fast pointer will eventually catch up to the slow pointer (the gap between them reduces by 1 each iteration).
Time Complexity: O(n)
Space Complexity: O(1)